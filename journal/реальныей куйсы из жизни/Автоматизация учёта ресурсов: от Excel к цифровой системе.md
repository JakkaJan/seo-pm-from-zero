# КЕЙС 1. Автоматизация учёта ресурсов: от Excel к цифровой системе

**Организация:** БашРО МООО РСО, Уфа  
**Период:** Июль — Сентябрь 2023  
**Роль:** PM / Business Analyst / Automation Engineer  
**Статус:** ✅ Завершён

---

## Проблема
Учёт расходных материалов, оборудования и продовольствия вёлся в разрозненных Excel-таблицах. Потери, двойные закупки, непрозрачность остатков.

## Ключевые результаты

| Метрика | Было | Стало |
|---------|------|-------|
| Время на учёт ресурсов | 100% | **−60%** |
| Расходы отделения | 100% | **−20%** |
| Превышение бюджета | Было | **0 ₽** |
| Срок реализации | — | **3 мес.** |

---

## Что было сделано

### 1. Аудит процессов
- Выявил 4 независимых источника данных (Excel, Google Sheets, бумажные журналы, 1С)
- Задокументировал user-flow сотрудников

### 2. Архитектура решения
Битрикс24 (Смарт-процессы + CRM)
↓ [REST API]
Python-скрипт (middleware)
↓ [REST API]
1С (система учёта)

### 3. Автоматические уведомления
- При остатке < 10 единиц любого ресурса → задача ответственному на пополнение

### 4. Дашборд для руководства
- Остатки по категориям
- Динамика расходов
- Прогноз закупок

### 5. Модули в 1С
- Ускорение формирования отчётов по остаткам на **70%**

---
##Навыки
#Python 3, REST API, JSON, Битрикс24, 1С, Процессный анализ, Дашборды
## Код: Python-скрипт синхронизации Битрикс24 ↔ 1С

```python
import requests
import json
from datetime import datetime

# Конфигурация
BITRIX_WEBHOOK = "https://company.bitrix24.ru/rest/1/WEBHOOK_TOKEN/"
ONEC_API_URL = "https://1c.company.ru/api/documents"

def sync_purchase_requests():
    """
    Заявки на закупку из Битрикс24 → 1С
    Создаёт документ "Требование на склад"
    """
    # Получаем новые заявки из Битрикс24
    response = requests.get(
        f"{BITRIX_WEBHOOK}crm.item.list",
        params={
            "entityTypeId": 171,  # Смарт-процесс "Закупки"
            "filter": {"stageId": "NEW"}
        }
    )
    
    requests_list = response.json().get("result", {}).get("items", [])
    
    for req in requests_list:
        # Формируем payload для 1С
        one_c_payload = {
            "document_type": "ТребованиеНаСклад",
            "date": datetime.now().isoformat(),
            "items": [
                {
                    "name": req["title"],
                    "quantity": req["ufCrmQuantity"],
                    "unit": req["ufCrmUnit"],
                    "responsible": req["assignedById"]
                }
            ],
            "source_id": req["id"]
        }
        
        # Отправляем в 1С
        one_c_response = requests.post(
            ONEC_API_URL,
            json=one_c_payload,
            headers={"Content-Type": "application/json"}
        )
        
        if one_c_response.status_code == 201:
            # Меняем статус в Битрикс24
            requests.post(
                f"{BITRIX_WEBHOOK}crm.item.update",
                json={
                    "entityTypeId": 171,
                    "id": req["id"],
                    "fields": {"stageId": "SYNCED"}
                }
            )
            print(f"✅ Заявка #{req['id']} синхронизирована")
        else:
            print(f"❌ Ошибка синхронизации #{req['id']}: {one_c_response.text}")

if __name__ == "__main__":
    sync_purchase_requests()



##Навыки
##Python 3, REST API, JSON, Битрикс24, 1С, Процессный анализ, Дашборды
