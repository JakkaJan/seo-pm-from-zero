<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Трекер подготовки к собеседованиям — E-commerce</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        .header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        .overall-progress {
            background: rgba(255,255,255,0.95);
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }

        .overall-progress h2 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.3rem;
        }

        .progress-bar-container {
            background: #e0e0e0;
            border-radius: 10px;
            height: 30px;
            overflow: hidden;
            position: relative;
        }

        .progress-bar {
            background: linear-gradient(90deg, #667eea, #764ba2);
            height: 100%;
            border-radius: 10px;
            transition: width 0.5s ease;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding-right: 10px;
            color: white;
            font-weight: bold;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .stat-card {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 15px;
            border-radius: 12px;
            text-align: center;
        }

        .stat-card .number {
            font-size: 2rem;
            font-weight: bold;
        }

        .stat-card .label {
            font-size: 0.9rem;
            opacity: 0.9;
        }

        .category {
            background: rgba(255,255,255,0.95);
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }

        .category-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            cursor: pointer;
        }

        .category-title {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .category-icon {
            width: 45px;
            height: 45px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }

        .category-title h3 {
            color: #333;
            font-size: 1.3rem;
        }

        .category-progress {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .mini-progress {
            width: 120px;
            height: 8px;
            background: #e0e0e0;
            border-radius: 4px;
            overflow: hidden;
        }

        .mini-progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 4px;
            transition: width 0.3s ease;
        }

        .toggle-btn {
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: #667eea;
            transition: transform 0.3s;
        }

        .toggle-btn.rotated {
            transform: rotate(180deg);
        }

        .questions-list {
            display: none;
        }

        .questions-list.active {
            display: block;
        }

        .question-item {
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 12px;
            transition: all 0.3s;
        }

        .question-item:hover {
            border-color: #667eea;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.15);
        }

        .question-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 10px;
        }

        .question-text {
            font-weight: 600;
            color: #333;
            flex: 1;
            margin-right: 15px;
        }

        .status-badges {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            cursor: pointer;
            transition: all 0.2s;
            border: 2px solid transparent;
        }

        .badge:hover {
            transform: scale(1.05);
        }

        .badge-not-started {
            background: #ffebee;
            color: #c62828;
        }

        .badge-learning {
            background: #fff3e0;
            color: #ef6c00;
        }

        .badge-learned {
            background: #e8f5e9;
            color: #2e7d32;
        }

        .badge-interview {
            background: #e3f2fd;
            color: #1565c0;
        }

        .answer-section {
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid #eee;
        }

        .answer-text {
            color: #555;
            line-height: 1.6;
            font-size: 0.95rem;
        }

        .answer-text ul {
            margin-left: 20px;
            margin-top: 8px;
        }

        .answer-text li {
            margin-bottom: 6px;
        }

        .add-question-btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 1rem;
            margin-top: 15px;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .add-question-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }

        .modal.active {
            display: flex;
        }

        .modal-content {
            background: white;
            border-radius: 16px;
            padding: 30px;
            width: 90%;
            max-width: 600px;
            max-height: 80vh;
            overflow-y: auto;
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .modal-header h3 {
            color: #333;
            font-size: 1.4rem;
        }

        .close-btn {
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: #999;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-weight: 500;
        }

        .form-group input,
        .form-group textarea,
        .form-group select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1rem;
            transition: border-color 0.2s;
        }

        .form-group input:focus,
        .form-group textarea:focus,
        .form-group select:focus {
            outline: none;
            border-color: #667eea;
        }

        .form-group textarea {
            min-height: 120px;
            resize: vertical;
        }

        .save-btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            width: 100%;
            transition: opacity 0.2s;
        }

        .save-btn:hover {
            opacity: 0.9;
        }

        .difficulty {
            display: inline-flex;
            gap: 3px;
            margin-left: 10px;
        }

        .difficulty-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #ddd;
        }

        .difficulty-dot.active {
            background: #ff9800;
        }

        .tips-section {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 12px;
            margin-top: 10px;
            font-size: 0.9rem;
            color: #666;
        }

        .tips-section strong {
            color: #333;
        }

        .export-import {
            display: flex;
            gap: 10px;
            margin-top: 20px;
            justify-content: center;
        }

        .export-import button {
            background: white;
            border: 2px solid #667eea;
            color: #667eea;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.2s;
        }

        .export-import button:hover {
            background: #667eea;
            color: white;
        }

        .search-box {
            width: 100%;
            padding: 12px 20px;
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            font-size: 1rem;
            margin-bottom: 20px;
            transition: border-color 0.2s;
        }

        .search-box:focus {
            outline: none;
            border-color: #667eea;
        }

        .priority-high {
            border-left: 4px solid #e53935;
        }

        .priority-medium {
            border-left: 4px solid #fb8c00;
        }

        .priority-low {
            border-left: 4px solid #43a047;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 1.8rem;
            }

            .category-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 10px;
            }

            .stats {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
<base target="_blank">
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 Трекер подготовки к собеседованиям</h1>
            <p>E-commerce | Платежные системы | CRM | Руководство проектами</p>
        </div>

        <div class="overall-progress">
            <h2>📊 Общий прогресс подготовки</h2>
            <div class="progress-bar-container">
                <div class="progress-bar" id="overallBar" style="width: 0%">0%</div>
            </div>
            <div class="stats">
                <div class="stat-card">
                    <div class="number" id="totalQuestions">0</div>
                    <div class="label">Всего вопросов</div>
                </div>
                <div class="stat-card">
                    <div class="number" id="learnedQuestions">0</div>
                    <div class="label">Изучено</div>
                </div>
                <div class="stat-card">
                    <div class="number" id="inProgress">0</div>
                    <div class="label">В процессе</div>
                </div>
                <div class="stat-card">
                    <div class="number" id="notStarted">0</div>
                    <div class="label">Не начато</div>
                </div>
            </div>
            <div class="export-import">
                <button onclick="exportData()">📥 Экспорт данных</button>
                <button onclick="document.getElementById('importFile').click()">📤 Импорт данных</button>
                <input type="file" id="importFile" style="display:none" accept=".json" onchange="importData(this)">
            </div>
        </div>

        <input type="text" class="search-box" id="searchBox" placeholder="🔍 Поиск по вопросам..." onkeyup="searchQuestions()">

        <div id="categoriesContainer"></div>
    </div>

    <div class="modal" id="questionModal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 id="modalTitle">Добавить вопрос</h3>
                <button class="close-btn" onclick="closeModal()">&times;</button>
            </div>
            <form id="questionForm" onsubmit="saveQuestion(event)">
                <div class="form-group">
                    <label>Категория</label>
                    <select id="categorySelect" required>
                        <option value="">Выберите категорию</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Вопрос</label>
                    <input type="text" id="questionInput" placeholder="Введите вопрос..." required>
                </div>
                <div class="form-group">
                    <label>Ответ / Ключевые моменты</label>
                    <textarea id="answerInput" placeholder="Напишите ответ или основные тезисы..."></textarea>
                </div>
                <div class="form-group">
                    <label>Статус</label>
                    <select id="statusSelect">
                        <option value="not-started">Не начато</option>
                        <option value="learning">В процессе изучения</option>
                        <option value="learned">Изучено</option>
                        <option value="interview">Отвечал на собеседовании</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Сложность (1-5)</label>
                    <select id="difficultySelect">
                        <option value="1">1 - Легко</option>
                        <option value="2">2</option>
                        <option value="3" selected>3 - Средне</option>
                        <option value="4">4</option>
                        <option value="5">5 - Сложно</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Дополнительные заметки / Советы</label>
                    <textarea id="tipsInput" placeholder="Дополнительная информация, советы, ссылки..."></textarea>
                </div>
                <button type="submit" class="save-btn">💾 Сохранить</button>
            </form>
        </div>
    </div>

    <script>
        let data = {
            categories: [
                {
                    id: 'ecommerce-payments',
                    name: '🛒 E-commerce & Платежные системы',
                    icon: '🛒',
                    color: '#e53935',
                    questions: [
                        {
                            id: 101,
                            text: 'Какой практический опыт нужен руководителю e-commerce?',
                            answer: `<strong>Обязательный опыт:</strong>
<ul>
<li>Практическая работа с онлайн-кассами и CRM-системами</li>
<li>Управление автоматизацией платежей и возвратов</li>
<li>Постановка задач разработчикам по интеграциям</li>
<li>Знание бизнес-процессов интернет-магазина</li>
<li>Опыт контроля качества и тестирования систем</li>
</ul>
<strong>Почему это критично:</strong> Без реального опыта сложно организовать процесс и гарантировать результат. Теории недостаточно — нужен подтверждённый практический опыт внедрения или использования подобных решений.`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'При ответе приведите конкретные примеры: какую CRM использовали, какие платёжные шлюзы интегрировали, какие автоматизации настроили. Интервьюер ищет доказательства реального опыта, а не теоретических знаний.'
                        },
                        {
                            id: 102,
                            text: 'Как должна работать CRM для e-commerce?',
                            answer: `<strong>Ключевые функции CRM в e-commerce:</strong>
<ul>
<li><strong>Учёт финансов:</strong> фиксация всех входящих платежей и возвратов в автоматическом режиме</li>
<li><strong>Автоматизация статусов:</strong> автоматическое изменение статусов заказов и платежей без ручного вмешательства</li>
<li><strong>Интеграция:</strong> прямая связь с платёжной системой и онлайн-кассой (54-ФЗ)</li>
<li><strong>История клиента:</strong> полная история взаимодействия с клиентом (заказы, платежи, обращения)</li>
<li><strong>Уведомления и отчёты:</strong> автоматические уведомления менеджерам и формирование финансовой отчётности</li>
</ul>
<strong>Главный принцип:</strong> CRM должна обеспечить полный контроль финансов и клиентских процессов в автоматическом режиме.`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Акцентируйте внимание на автоматизации: как только клиент платит — система фиксирует это в CRM и запускает бизнес-процессы. Возврат оформляется через пару кликов, все данные фиксируются без ручного ввода.'
                        },
                        {
                            id: 103,
                            text: 'Какие навыки нужны руководителю для разработки ПО платежей?',
                            answer: `<strong>Бизнес-навыки:</strong>
<ul>
<li>Понимание процессов приёма и возврата платежей</li>
<li>Знание CRM для учёта платежей и возвратов</li>
<li>Контроль логики обработки транзакций и отчётности</li>
</ul>
<strong>Технические навыки:</strong>
<ul>
<li>Интеграция с онлайн-кассами по 54-ФЗ</li>
<li>Требования к безопасности: PCI DSS, шифрование, защита персональных данных (152-ФЗ)</li>
<li>Постановка задач разработчикам API и backend</li>
<li>Проверка архитектуры: надёжность, масштабируемость, интеграция с CRM и кассой</li>
</ul>
<strong>Тестирование:</strong>
<ul>
<li>Проведение тестовых платежей и эмуляция ошибок</li>
<li>Сценарии обработки неуспешных платежей и возвратов</li>
<li>Ведение логов транзакций</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Подчеркните, что вы понимаете НЕ только бизнес-процессы, но и технические детали: протоколы VISA/MasterCard, Apple Pay/Google Pay, шифрование, архитектуру. Это критично для успеха e-commerce проекта.'
                        },
                        {
                            id: 104,
                            text: 'Что такое 54-ФЗ и какие требования к онлайн-кассам?',
                            answer: `<strong>54-ФЗ «О применении контрольно-кассовой техники»:</strong>
<ul>
<li>Обязательность применения онлайн-касс при приёме платежей от физических лиц</li>
<li>Передача фискальных данных в ФНС в реальном времени через ОФД (оператор фискальных данных)</li>
<li>Формирование фискального чека (БСО) и отправка его клиенту (email/SMS/бумага)</li>
</ul>
<strong>Требования к интеграции:</strong>
<ul>
<li>Касса должна быть зарегистрирована в ФНС и подключена к ОФД</li>
<li>При каждой транзакции формируется фискальный документ с уникальным номером (ФД) и признаком расчёта</li>
<li>Поддержка разных систем налогообложения (ОСН, УСН, ЕНВД и др.)</li>
<li>Возвраты также фискализируются — формируется чек на возврат</li>
</ul>
<strong>Последствия нарушения:</strong> штрафы до 50% суммы расчёта без ККТ, приостановка деятельности.`,
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Упомяните конкретные модели касс, с которыми работали (Атол, Эвотор, Штрих-М). Объясните разницу между фискальным накопителем (ФН) и ОФД. Покажите понимание полного цикла: платёж → фискализация → отчётность.'
                        },
                        {
                            id: 105,
                            text: 'Что такое PCI DSS и почему это важно для платежей?',
                            answer: `<strong>PCI DSS (Payment Card Industry Data Security Standard):</strong>
<ul>
<li>Международный стандарт безопасности данных платёжных карт</li>
<li>Обязателен для всех, кто принимает, обрабатывает, передаёт или хранит данные карт</li>
</ul>
<strong>Ключевые требования:</strong>
<ul>
<li><strong>Шифрование:</strong> передача данных по TLS/SSL, шифрование хранимых данных (AES-256)</li>
<li><strong>Сегментация сети:</strong> изоляция систем, обрабатывающих карточные данные (CDE)</li>
<li><strong>Контроль доступа:</strong> многофакторная аутентификация, принцип минимальных привилегий</li>
<li><strong>Мониторинг:</strong> логирование всех операций с данными карт, регулярное сканирование уязвимостей</li>
<li><strong>Тестирование:</strong> регулярные пентесты и аудиты безопасности</li>
</ul>
<strong>Уровни комплаенса:</strong> Level 1 (>6M транзакций/год) — QSA-аудит; Level 2-4 — SAQ (самооценка).
<strong>Последствия нарушения:</strong> штрафы от $5,000 до $100,000/мес, потеря права принимать карты, репутационные потери.`,
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Если компания разрабатывает собственный софт для платежей — PCI DSS Level 1 обязателен. Упомяните токенизацию и использование платёжных провайдеров (Stripe, CloudPayments) для снижения scope комплаенса.'
                        },
                        {
                            id: 106,
                            text: 'Как организовать автоматизацию возвратов в e-commerce?',
                            answer: `<strong>Бизнес-логика возвратов:</strong>
<ul>
<li>Клиент инициирует возврат через ЛК или обращение в поддержку</li>
<li>CRM автоматически проверяет условия возврата (срок, состояние товара, платёжная система)</li>
<li>Менеджер подтверждает возврат в CRM — система автоматически отправляет запрос в платёжный шлюз</li>
<li>Платёжный шлюз обрабатывает возврат на исходную карту/кошелёк (сроки зависят от банка: 3-30 дней)</li>
<li>CRM фиксирует статус возврата, обновляет остатки на складе, отправляет уведомление клиенту</li>
</ul>
<strong>Технические детали:</strong>
<ul>
<li>Интеграция API платёжного шлюза для refund/chargeback</li>
<li>Фискализация возврата через онлайн-кассу (чек «возврат прихода»)</li>
<li>Обработка частичных возвратов и возвратов при разных способах оплаты (карта, СБП, электронные кошельки)</li>
<li>Автоматические отчёты по возвратам для бухгалтерии</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Подчеркните, что возврат должен быть «в пару кликов». Покажите понимание разницы между refund (добровольный возврат) и chargeback (принудительный через банк). Упомяните комиссии платёжных систем при возвратах.'
                        },
                        {
                            id: 107,
                            text: 'Как правильно ставить задачи разработчикам по интеграции платежей?',
                            answer: `<strong>Структура технического задания:</strong>
<ul>
<li><strong>Бизнес-требования:</strong> какие платёжные методы поддерживать (карты, СБП, Apple Pay), какие валюты, гео</li>
<li><strong>Интеграционные требования:</strong> API платёжного шлюза, онлайн-касса, CRM, учётная система</li>
<li><strong>Логика обработки:</strong> сценарии успешной оплаты, неуспешной, таймаутов, повторных попыток, idempotency</li>
<li><strong>Безопасность:</strong> PCI DSS scope, шифрование, токенизация, валидация входящих данных</li>
<li><strong>Тестирование:</strong> тестовые карты, эмуляция ошибок (insufficient funds, expired card), нагрузочное тестирование</li>
<li><strong>Мониторинг:</strong> логи транзакций, алерты при сбоях, дашборды успешности платежей</li>
</ul>
<strong>Формат постановки:</strong>
<ul>
<li>User Story + Acceptance Criteria (Given/When/Then)</li>
<li>Sequence diagram для платёжного flow</li>
<li>Моки/API spec платёжного провайдера</li>
<li>Критерии готовности (Definition of Done)</li>
</ul>
<strong>Контроль:</strong> code review с фокусом на безопасность, интеграционное тестирование с реальными тестовыми платежами, проверка обработки edge cases.`,
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Покажите, что вы понимаете разницу между бизнес-требованиями и техническими. Приведите пример конкретного ТЗ, которое вы писали. Упомяните idempotency keys — это показатель глубокого понимания платёжных систем.'
                        },
                        {
                            id: 108,
                            text: 'Как выбрать и внедрить CRM для e-commerce?',
                            answer: `<strong>Популярные CRM для e-commerce:</strong>
<ul>
<li><strong>Битрикс24:</strong> тесная интеграция с 1С-Битрикс, готовые модули для интернет-магазинов, встроенная телефония</li>
<li><strong>amoCRM:</strong> простота настройки, визуальные воронки продаж, большое количество интеграций через marketplace</li>
<li><strong>RetailCRM:</strong> специализированная CRM именно для e-commerce: учёт остатков, интеграция с маркетплейсами, RFM-аналитика</li>
</ul>
<strong>Критерии выбора:</strong>
<ul>
<li>Наличие открытого API для интеграции с сайтом, платёжными системами, кассами</li>
<li>Возможность автоматизации продаж (триггеры, роботы, бизнес-процессы)</li>
<li>Управление лидами и клиентской базой (сегментация, история заказов)</li>
<li>Клиентская поддержка (тикет-система, чаты, телефония)</li>
<li>Отчётность и аналитика (воронка продаж, конверсия, LTV)</li>
</ul>
<strong>Внедрение:</strong>
<ol>
<li>Аудит текущих процессов и выбор CRM под задачи</li>
<li>Настройка воронок продаж, статусов заказов, полей клиентов</li>
<li>Интеграция с сайтом (API/webhooks) — передача заказов, статусов, платежей</li>
<li>Интеграция с платёжными системами и онлайн-кассой</li>
<li>Обучение команды, написание регламентов</li>
<li>Тестирование полного цикла: заказ → оплата → фискализация → CRM → доставка</li>
</ol>`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Для позиции руководителя важно показать, что вы понимаете разницу между CRM "для всех" и специализированной для e-commerce. RetailCRM — сильный козырь, так как она создана именно для интернет-торговли.'
                        },
                        {
                            id: 109,
                            text: 'Какие юридические требования нужно знать руководителю e-commerce?',
                            answer: `<strong>54-ФЗ — применение ККТ:</strong>
<ul>
<li>Обязательность онлайн-касс при приёме платежей от физлиц</li>
<li>Фискальные данные передаются в ФНС через ОФД в реальном времени</li>
<li>Формирование фискального чека (БСО) и отправка клиенту</li>
<li>Возвраты также фискализируются — чек «возврат прихода»</li>
<li>Штрафы за нарушение: до 50% суммы расчёта без ККТ</li>
</ul>
<strong>152-ФЗ — персональные данные:</strong>
<ul>
<li>Обязательное согласие на обработку ПД при оформлении заказа</li>
<li>Шифрование и защита ПД клиентов (хранение, передача)</li>
<li>Назначение ответственного за обработку ПД</li>
</ul>
<strong>Закон о рекламе:</strong>
<ul>
<li>Маркировка рекламы (если используете блогеров/аффилиатов)</li>
<li>Запрет на недостоверную рекламу (цену указывать с учётом всех сборов)</li>
</ul>
<strong>Закон о защите прав потребителей:</strong>
<ul>
<li>Право на возврат товара надлежащего качества в течение 7 дней (14 дней для дистанционной торговли)</li>
<li>Обязательная информация о продавце на сайте (реквизиты, ИНН, ОГРН)</li>
<li>Публичная оферта — обязательный договор на сайте</li>
</ul>
<strong>Кассовая дисциплина:</strong>
<ul>
<li>Регистрация кассы в ФНС, замена ФН (фискального накопителя) в срок</li>
<li>Ежедневное закрытие смены и формирование Z-отчёта</li>
<li>Хранение фискальных данных не менее 5 лет</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Покажите, что вы понимаете не только технические, но и юридические риски. Упомяните, что проверяли compliance при выборе платёжных провайдеров и кассовых решений.'
                        },
                        {
                            id: 110,
                            text: 'Как организовать полный цикл интернет-магазина?',
                            answer: `<strong>1. Каталог и контент:</strong>
<ul>
<li>Структура категорий, фильтры, карточки товаров (фото, описания, характеристики)</li>
<li>Синхронизация с учётной системой (1С, МойСклад) — остатки, цены</li>
</ul>
<strong>2. Корзина и оформление заказа:</strong>
<ul>
<li>Удобная корзина с редактированием, промокодами, расчётом доставки</li>
<li>Оформление без регистрации (гостевой checkout) и с регистрацией</li>
<li>Выбор способа доставки (курьер, ПВЗ, самовывоз) и оплаты</li>
</ul>
<strong>3. Платёжный шлюз:</strong>
<ul>
<li>Приём платежей (карты, СБП, электронные кошельки)</li>
<li>3D Secure, токенизация, обработка ошибок</li>
<li>Автоматическое подтверждение/отмена заказа по статусу платежа</li>
</ul>
<strong>4. Онлайн-касса и фискализация:</strong>
<ul>
<li>Автоматическая фискализация при подтверждении оплаты</li>
<li>Отправка чека клиенту (email/SMS)</li>
<li>Передача данных в ОФД и ФНС</li>
</ul>
<strong>5. CRM и обработка заказа:</strong>
<ul>
<li>Автоматическое создание заказа в CRM со статусом «оплачен»</li>
<li>Маршрутизация заказа менеджеру/на склад</li>
<li>Обновление статусов (собран, передан в доставку, доставлен)</li>
</ul>
<strong>6. Логистика и доставка:</strong>
<ul>
<li>Интеграция со службами доставки (СДЭК, Boxberry, Почта России)</li>
<li>Трекинг-номера, уведомления клиенту</li>
</ul>
<strong>7. Возвраты и поддержка:</strong>
<ul>
<li>Автоматизация возвратов через CRM</li>
<li>Тикет-система, чат, телефония для поддержки клиентов</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Нарисуйте схему на листе бумаге или в Miro — это покажет системное мышление. Подчеркните, что вы понимаете связи между блоками: платёж → касса → CRM → склад → доставка.'
                        },
                        {
                            id: 111,
                            text: 'Как проводить тестовые интеграции онлайн-кассы и CRM?',
                            answer: `<strong>Подготовка:</strong>
<ul>
<li>Создать тестовый магазин/стенд (dev/staging environment)</li>
<li>Получить тестовые доступы к API платёжного шлюза и кассы</li>
<li>Подготовить тестовые данные: товары, цены, тестовые карты (4111 1111 1111 1111 для Visa)</li>
</ul>
<strong>Сценарии тестирования:</strong>
<ol>
<li><strong>Успешная оплата:</strong> заказ → оплата → фискализация → обновление CRM → уведомление клиенту</li>
<li><strong>Неуспешная оплата:</strong> недостаточно средств, просроченная карта — проверка обработки ошибок и сообщений клиенту</li>
<li><strong>Таймаут:</strong> имитация задержки ответа от платёжного шлюза — проверка retry logic и idempotency</li>
<li><strong>Дублирование:</strong> повторный запрос с тем же idempotency key — проверка отсутствия двойного списания</li>
<li><strong>Возврат:</strong> инициация возврата в CRM → refund API → фискализация возврата → обновление статуса</li>
<li><strong>Ошибка кассы:</strong> имитация недоступности ОФД — проверка очереди и повторной отправки фискальных данных</li>
</ol>
<strong>Чек-лист проверки:</strong>
<ul>
<li>Фискальный чек сформирован корректно (ИНН, название, цена, НДС)</li>
<li>Данные дошли до ОФД и отображаются в личном кабинете ФНС</li>
<li>CRM получила корректный статус заказа и платежа</li>
<li>Клиент получил email/SMS с чеком и подтверждением</li>
<li>Логи содержат все этапы обработки транзакции</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Упомяните конкретные инструменты: Postman для API-тестов, тестовые среды платёжных провайдеров (CloudPayments test mode), эмуляторы онлайн-касс. Это покажет hands-on опыт.'
                        }
                    ]
                },
                {
                    id: 'behavioral',
                    name: 'Поведенческие вопросы (Soft Skills)',
                    icon: '🧠',
                    color: '#ff6b6b',
                    questions: [
                        {
                            id: 1,
                            text: 'Расскажите о себе',
                            answer: 'Кратко: опыт, ключевые достижения, почему эта роль. 1-2 минуты.',
                            status: 'not-started',
                            difficulty: 2,
                            tips: 'Подготовьте 3 версии: 30 сек, 1 мин, 2 мин. Фокус на релевантном опыте.'
                        },
                        {
                            id: 2,
                            text: 'Ваши сильные и слабые стороны?',
                            answer: 'Сильные: 3 качества с примерами. Слабые: реальная область роста + что делаете для улучшения.',
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Не говорите "перфекционист" — это клише. Выберите что-то конкретное и покажите прогресс.'
                        },
                        {
                            id: 3,
                            text: 'Почему хотите работать у нас?',
                            answer: 'Исследуйте компанию: продукты, культура, технологии. Свяжите со своими целями.',
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Никогда не говорите "потому что вы большая компания". Будьте конкретны.'
                        },
                        {
                            id: 201,
                            text: 'Расскажите о вашем опыте управления e-commerce проектами',
                            answer: `<strong>Используйте STAR-метод:</strong>
<ul>
<li><strong>Situation:</strong> контекст проекта (размер магазина, оборот, команда)</li>
<li><strong>Task:</strong> ваша задача как руководителя (запуск, масштабирование, автоматизация)</li>
<li><strong>Action:</strong> конкретные шаги — выбор CRM, интеграция платежей, постановка задач разработчикам</li>
<li><strong>Result:</strong> измеримый результат (% роста конверсии, сокращение времени обработки заказов, снижение ошибок)</li>
</ul>
<strong>Пример:</strong> "Запустил интернет-магазин с нуля: выбрал CRM (Bitrix24/RetailCRM), интегрировал платёжный шлюз и онлайн-кассу по 54-ФЗ, автоматизировал возвраты. Результат: время обработки заказа сократилось с 2 часов до 15 минут, ошибки при фискализации уменьшились на 90%."`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Готовьте 3-5 историй заранее. Всегда заканчивайте конкретным результатом (% улучшения, $ экономии, время). Интервьюер ищет доказательства, а не общие фразы.'
                        },
                        {
                            id: 202,
                            text: 'Как вы контролируете качество при интеграции платежных систем?',
                            answer: `<strong>Многоуровневый контроль:</strong>
<ul>
<li><strong>Планирование:</strong> чёткое ТС с acceptance criteria, sequence diagram, edge cases</li>
<li><strong>Code review:</strong> проверка безопасности (SQL-инъекции, XSS), валидация входных данных, обработка ошибок</li>
<li><strong>Тестирование:</strong> unit-тесты, интеграционные тесты с тестовыми платежами, нагрузочное тестирование</li>
<li><strong>Staging:</strong> полный цикл на тестовом окружении: оплата → фискализация → возврат → отчётность</li>
<li><strong>Мониторинг:</strong> логи всех транзакций, алерты при ошибках, дашборд успешности платежей</li>
<li><strong>Post-production:</strong> анализ первых 100 реальных транзакций, быстрый rollback-план</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Покажите системный подход. Упомяните конкретные инструменты: Jira для задач, GitLab CI для автотестов, Kibana/Grafana для мониторинга, Postman для API-тестирования.'
                        },
                        {
                            id: 203,
                            text: 'Какие навыки нужны руководителю e-commerce проекта?',
                            answer: `<strong>Бизнес-навыки:</strong>
<ul>
<li>Понимание полного цикла интернет-магазина: от каталога до оплаты и доставки</li>
<li>Знание юридических требований: 54-ФЗ, кассовая дисциплина, защита прав потребителей</li>
<li>Управление бизнес-процессами и командой</li>
</ul>
<strong>Технические навыки:</strong>
<ul>
<li>Опыт работы с онлайн-кассами: интеграция, отчётность, фискализация</li>
<li>Понимание CRM: выбор, настройка, автоматизация продаж (Битрикс24, amoCRM, RetailCRM)</li>
<li>Архитектура интернет-магазина: каталог, корзина, оформление заказа, интеграции</li>
<li>Постановка задач разработчикам: формулировка ТЗ, контроль сроков, code review</li>
</ul>
<strong>На практике:</strong>
<ul>
<li>Проведение тестовых интеграций онлайн-кассы и CRM на демо-проекте</li>
<li>Составление чек-листа систем и процессов для запуска магазина</li>
<li>Изучение реальных кейсов внедрения e-commerce в России</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Этот вопрос — обобщение вашей экспертизы. Отвечайте структурированно: бизнес → технологии → процессы. Приводите конкретные названия систем и примеры задач, которые ставили разработчикам.'
                        }
                    ]
                },
                {
                    id: 'technical',
                    name: 'Технические вопросы',
                    icon: '💻',
                    color: '#4ecdc4',
                    questions: [
                        {
                            id: 4,
                            text: 'Что такое REST API?',
                            answer: 'Архитектурный стиль: ресурсы, HTTP методы (GET/POST/PUT/DELETE), stateless, JSON/XML.',
                            status: 'not-started',
                            difficulty: 2,
                            tips: 'Приведите примеры кодов статусов (200, 404, 500). Объясните разницу REST vs SOAP.'
                        },
                        {
                            id: 5,
                            text: 'Объясните принципы SOLID',
                            answer: 'S - Single Responsibility, O - Open/Closed, L - Liskov Substitution, I - Interface Segregation, D - Dependency Inversion',
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Для каждого принципа приведите пример из практики. Покажите, как нарушение влияет на код.'
                        },
                        {
                            id: 301,
                            text: 'Какие протоколы и API используются в платёжных системах?',
                            answer: `<strong>Протоколы приёма платежей:</strong>
<ul>
<li><strong>HTTP/HTTPS REST API:</strong> основной способ интеграции с платёжными шлюзами (JSON/XML)</li>
<li><strong>Webhooks:</strong> асинхронные уведомления о статусе платежа от шлюза к merchant</li>
<li><strong>3D Secure 2.0:</strong> протокол аутентификации держателя карты (перенаправление на страницу банка)</li>
<li><strong>Tokenization:</strong> замена PAN (номера карты) на токен для безопасного хранения</li>
</ul>
<strong>Специфические API:</strong>
<ul>
<li><strong>PCI DSS compliant API:</strong> прямая интеграция с процессингом (высокие требования к безопасности)</li>
<li><strong>Hosted Payment Page (HPP):</strong> перенаправление на страницу провайдера (снижает PCI scope)</li>
<li><strong>Server-to-Server (S2S):</strong> прямая передача данных с вашего сервера (требует PCI DSS Level 1)</li>
<li><strong>СБП (Система Быстрых Платежей ЦБ РФ):</strong> API для QR-платежей и переводов по телефону</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Объясните разницу между HPP и S2S с точки зрения PCI DSS scope. Упомяните idempotency keys для предотвращения двойных списаний. Покажите понимание webhook retry logic и обработки timeout.'
                        },
                        {
                            id: 302,
                            text: 'Как обеспечить безопасность платёжных данных?',
                            answer: `<strong>Технические меры:</strong>
<ul>
<li><strong>Шифрование:</strong> TLS 1.2+ для передачи, AES-256 для хранения чувствительных данных</li>
<li><strong>Токенизация:</strong> не хранить PAN, использовать токены от платёжного провайдера</li>
<li><strong>Валидация:</strong> проверка входных данных (CVV, срок действия, Luhn algorithm), защита от SQL-инъекций и XSS</li>
<li><strong>Сегментация:</strong> изоляция CDE (Cardholder Data Environment) — отдельная сеть, ограниченный доступ</li>
</ul>
<strong>Организационные меры:</strong>
<ul>
<li>PCI DSS compliance (Level 1 — QSA аудит, Level 2-4 — SAQ)</li>
<li>Многофакторная аутентификация для доступа к платёжным системам</li>
<li>Регулярные пентесты и сканирование уязвимостей</li>
<li>Логирование всех операций с данными карт, мониторинг аномалий</li>
</ul>
<strong>Законодательство РФ:</strong> 152-ФЗ о персональных данных — обязательное шифрование и защита ПД клиентов.`,
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Если компания не хочет проходить полный PCI DSS audit — используйте HPP (Hosted Payment Page) или токенизацию от провайдера. Это снижает scope до SAQ A (самооценка из 22 пункта вместо 300+).'
                        },
                        {
                            id: 303,
                            text: 'Какие платформы e-commerce существуют и как выбрать?',
                            answer: `<strong>SaaS-платформы (облачные):</strong>
<ul>
<li><strong>Shopify:</strong> лидер мирового рынка, простота запуска, огромный marketplace приложений, хостинг включён. Минусы: комиссия + абонплата, ограниченная кастомизация для сложных бизнес-процессов</li>
<li><strong>Tilda, Wix:</strong> для малого бизнеса, простые каталоги, ограниченные интеграции</li>
</ul>
<strong>Open Source (self-hosted):</strong>
<ul>
<li><strong>WooCommerce (WordPress):</strong> гибкость, огромное комьюнити, бесплатный базовый функционал. Минусы: требует оптимизации под нагрузку, безопасность на хозяине</li>
<li><strong>Magento (Adobe Commerce):</strong> enterprise-уровень, максимальная кастомизация, мультистор, B2B. Минусы: высокая стоимость разработки и поддержки, требовательна к ресурсам</li>
</ul>
<strong>Российские платформы:</strong>
<ul>
<li><strong>1С-Битрикс:</strong> лидер РФ, тесная интеграция с 1С, готовые модули под 54-ФЗ, русскоязычная поддержка. Минусы: лицензионная стоимость, требует опытных разработчиков</li>
<li><strong>InSales, Shop-Script (Webasyst):</strong> российские аналоги Shopify с адаптацией под местный рынок</li>
</ul>
<strong>Критерии выбора:</strong>
<ul>
<li>Бюджет (CAPEX vs OPEX)</li>
<li>Масштаб (SKU, трафик, география)</li>
<li>Интеграции (1С, CRM, кассы, доставка)</li>
<li>Команда (есть ли разработчики под конкретный стек)</li>
<li>Требования к кастомизации (уникальные бизнес-процессы)</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Для российского рынка упомяните 1С-Битрикс как стандарт де-факто для среднего и крупного бизнеса. Если компания планирует собственную разработку — обсудите headless/composable commerce (API-first архитектура).'
                        },
                        {
                            id: 304,
                            text: 'Какие метрики и аналитика важны для e-commerce?',
                            answer: `<strong>Метрики воронки продаж:</strong>
<ul>
<li><strong>Конверсия:</strong> посетители → добавление в корзину → оформление заказа → оплата (типичная воронка: 100% → 8-15% → 3-5% → 2-4%)</li>
<li><strong>Средний чек (AOV):</strong> выручка / количество заказов</li>
<li><strong>LTV (Lifetime Value):</strong> суммарная прибыль от клиента за всё время</li>
<li><strong>CAC (Customer Acquisition Cost):</strong> стоимость привлечения одного клиента</li>
</ul>
<strong>Метрики платежей:</strong>
<ul>
<li>Успешность платежей (authorization rate)</li>
<li>Доля возвратов и chargeback rate</li>
<li>Среднее время возврата</li>
<li>Комиссии платёжных систем как % от выручки</li>
</ul>
<strong>Инструменты аналитики:</strong>
<ul>
<li><strong>Google Analytics 4 / Яндекс.Метрика:</strong> трафик, поведение, конверсия, воронка</li>
<li><strong>BI-системы:</strong> Power BI, Tableau, Яндекс.DataLens — сквозная аналитика</li>
<li><strong>A/B тесты:</strong> Google Optimize, VWO — тестирование цен, описаний, процесса оформления</li>
</ul>
<strong>ROI маркетинговых каналов:</strong>
<ul>
<li>Расчёт ROI по каждому каналу (SEO, контекст, таргет, email)</li>
<li>Attribution modeling (last-click vs multi-touch)</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Покажите, что вы понимаете не только технические метрики, но и бизнесовые. Упомяните RFM-анализ (Recency, Frequency, Monetary) для сегментации клиентской базы — это показатель зрелости.'
                        },
                        {
                            id: 305,
                            text: 'Как организовать Agile/Scrum для e-commerce команды?',
                            answer: `<strong>Структура команды e-commerce:</strong>
<ul>
<li>Product Owner (вы или бизнес-заказчик) — приоритизация бэклога</li>
<li>Scrum Master — фасилитация процесса, устранение блокеров</li>
<li>Команда разработки: backend, frontend, DevOps, QA</li>
<li>Stakeholders: маркетинг, бухгалтерия, служба поддержки</li>
</ul>
<strong>Процессы:</strong>
<ul>
<li><strong>Спринты:</strong> 2 недели — оптимально для e-commerce (быстрые релизы, реакция на рынок)</li>
<li><strong>Планирование:</strong> оценка story points, приоритизация по MoSCoW (Must/Should/Could/Won't)</li>
<li><strong>Ежедневные stand-ups:</strong> 15 минут — что сделано, что планируется, блокеры</li>
<li><strong>Sprint Review:</strong> демо для бизнеса — новые фичи, интеграции, автоматизации</li>
<li><strong>Ретроспектива:</strong> что пошло хорошо, что улучшить, action items</li>
</ul>
<strong>Бэклог e-commerce проекта:</strong>
<ul>
<li>Epic: "Запуск платёжной системы" → Stories: интеграция API, 3D Secure, тестирование, фискализация</li>
<li>Epic: "Автоматизация возвратов" → Stories: UI для менеджера, API refund, обновление CRM, уведомления</li>
<li>Технический долг: рефакторинг, обновление зависимостей, улучшение мониторинга</li>
</ul>
<strong>Инструменты:</strong>
<ul>
<li>Jira / Trello / YouTrack для задач</li>
<li>Confluence / Notion для документации</li>
<li>Slack / Telegram для коммуникаций</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Покажите баланс между гибкостью Agile и необходимостью документации для платёжных систем (PCI DSS требует документирование процессов). Упомяните Kanban для операционной поддержки (баги, инциденты).'
                        },
                        {
                            id: 306,
                            text: 'Какие маркетинговые каналы нужно знать руководителю e-commerce?',
                            answer: `<strong>Органический трафик:</strong>
<ul>
<li><strong>SEO:</strong> оптимизация структуры сайта, метаданных, скорости загрузки (Core Web Vitals), контент-стратегия</li>
<li><strong>Email-маркетинг:</strong> welcome-цепочки, брошенная корзина, триггерные рассылки (OpenRate 15-25%, CTR 2-5%)</li>
<li><strong>SMM:</strong> контент в соцсетях, работа с сообществами, UGC (контент пользователей)</li>
</ul>
<strong>Платный трафик:</strong>
<ul>
<li><strong>Контекстная реклама (PPC):</strong> Яндекс.Директ, Google Ads — поиск, РСЯ, ремаркетинг</li>
<li><strong>Таргетированная реклама:</strong> ВКонтакте, myTarget, Instagram/Facebook (если гео позволяет)</li>
<li><strong>CPA-сети:</strong> Admitad, CityAds — оплата за конкретное действие (продажа, лид)</li>
</ul>
<strong>Удержание и рост:</strong>
<ul>
<li><strong>CRM-маркетинг:</strong> сегментация, персонализация, RFM-анализ</li>
<li><strong>Программы лояльности:</strong> кэшбэк, баллы, реферальные программы</li>
<li><strong>A/B тесты:</strong> цены, заголовки, CTA-кнопки, процесс оформления</li>
</ul>
<strong>Руководителю важно понимать:</strong>
<ul>
<li>Unit-экономику каждого канала (CAC, ROI)</li>
<li>Взаимосвязь каналов (multi-touch attribution)</li>
<li>Сезонность и планирование бюджетов</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Вы не обязаны быть экспертом по каждому каналу, но должны понимать их эффективность и взаимосвязь. Упомяните, что координировали работу с маркетинговым агентством или внутренней командой.'
                        },
                        {
                            id: 307,
                            text: 'Как управлять клиентским сервисом, поддержкой и возвратами?',
                            answer: `<strong>Каналы поддержки:</strong>
<ul>
<li>Телефон (виртуальная АТС интегрированная с CRM)</li>
<li>Онлайн-чат (на сайте, в мессенджерах: Telegram, WhatsApp, ВКонтакте)</li>
<li>Email / тикет-система (встроена в CRM)</li>
<li>Социальные сети и отзывы</li>
</ul>
<strong>Автоматизация поддержки:</strong>
<ul>
<li>Чат-боты для типовых вопросов (статус заказа, условия доставки, возврат)</li>
<li>База знаний / FAQ на сайте</li>
<li>Автоматическая маршрутизация обращений по темам и приоритетам</li>
</ul>
<strong>Процесс возврата:</strong>
<ol>
<li>Клиент инициирует возврат (через ЛК, чат, телефон)</li>
<li>CRM проверяет условия (срок, состояние, категория товара)</li>
<li>Менеджер подтверждает → CRM запускает refund через платёжный шлюз</li>
<li>Автоматическая фискализация возврата через онлайн-кассу</li>
<li>Обновление остатков на складе (интеграция с учётной системой)</li>
<li>Уведомление клиенту о статусе возврата и сроках зачисления</li>
</ol>
<strong>Метрики поддержки:</strong>
<ul>
<li>SLA: время первого ответа (< 15 мин), время решения (< 24 часов)</li>
<li>CSAT (Customer Satisfaction Score) — оценка после диалога</li>
<li>NPS (Net Promoter Score) — лояльность клиентов</li>
<li>Доля повторных обращений по одному вопросу (FCR — First Contact Resolution)</li>
</ul>
<strong>Юридические аспекты:</strong>
<ul>
<li>Закон о защите прав потребителей: 14 дней на возврат без объяснений (дистанционная торговля)</li>
<li>Прозрачная политика возвратов на сайте (публичная оферта)</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Подчеркните, что клиентский сервис — это не только затраты, но и источник инсайтов. Анализ причин возвратов и обращений помогает улучшить продукт, описания товаров и процессы.'
                        }
                    ]
                },
                {
                    id: 'system-design',
                    name: 'System Design',
                    icon: '🏗️',
                    color: '#45b7d1',
                    questions: [
                        {
                            id: 6,
                            text: 'Спроектируйте URL shortener',
                            answer: '1) Требования (функциональные/нефункциональные) 2) API 3) БД (SQL vs NoSQL) 4) Хеширование 5) Масштабирование',
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Начинайте с требований. Спросите объемы: сколько URL в день, сколько чтений.'
                        },
                        {
                            id: 401,
                            text: 'Спроектируйте архитектуру платёжной системы для интернет-магазина',
                            answer: `<strong>1. Требования:</strong>
<ul>
<li><strong>Функциональные:</strong> приём платежей (карты, СБП, электронные кошельки), возвраты, рекуррентные платежи, фискализация</li>
<li><strong>Нефункциональные:</strong> 99.99% uptime, обработка 1000 TPS, latency < 500ms, PCI DSS compliance</li>
</ul>
<strong>2. Компоненты:</strong>
<ul>
<li><strong>API Gateway:</strong> маршрутизация, rate limiting, аутентификация, WAF</li>
<li><strong>Payment Service:</strong> бизнес-логика: валидация, маршрутизация платежа к шлюзу, idempotency</li>
<li><strong>Payment Gateway Adapter:</strong> абстракция над разными провайдерами (Stripe, CloudPayments, СБП)</li>
<li><strong>Fiscal Service:</strong> интеграция с онлайн-кассой, формирование фискальных чеков, отправка в ОФД</li>
<li><strong>CRM Integration:</strong> обновление статусов заказов, история платежей</li>
<li><strong>Notification Service:</strong> email/SMS уведомления клиентам и менеджерам</li>
</ul>
<strong>3. Базы данных:</strong>
<ul>
<li><strong>PostgreSQL:</strong> транзакционные данные (ACID важен для платежей)</li>
<li><strong>Redis:</strong> кэширование сессий, idempotency keys, rate limiting</li>
<li><strong>Kafka/RabbitMQ:</strong> асинхронная обработка (фискализация, уведомления, аналитика)</li>
</ul>
<strong>4. Безопасность:</strong>
<ul>
<li>WAF, DDoS protection, TLS 1.3, токенизация карт, сегментация CDE</li>
</ul>
<strong>5. Мониторинг:</strong>
<ul>
<li>Prometheus + Grafana для метрик, ELK для логов, PagerDuty для алертов</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 5,
                            tips: 'Ключевой момент — idempotency. При повторном запросе с тем же ключом система должна вернуть тот же результат, не создавая дубль. Также обсудите saga pattern для распределённых транзакций (платёж → фискализация → CRM → склад).'
                        }
                    ]
                },
                {
                    id: 'projects',
                    name: 'Вопросы о проектах',
                    icon: '📁',
                    color: '#feca57',
                    questions: [
                        {
                            id: 8,
                            text: 'Расскажите о самом сложном проекте',
                            answer: 'STAR метод: Situation (контекст), Task (задача), Action (ваши действия), Result (результат с метриками).',
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Готовьте 3-5 историй заранее. Всегда заканчивайте конкретным результатом (% улучшения, $ экономии).'
                        },
                        {
                            id: 501,
                            text: 'Опишите проект по интеграции CRM с платёжной системой и онлайн-кассой',
                            answer: `<strong>Situation:</strong>
Интернет-магазин с оборотом 50 млн/год работал на ручной обработке заказов. Менеджеры вручную проверяли платежи в личном кабинете банка, фискализировали чеки через отдельный софт, возвраты занимали 3-5 дней.

<strong>Task:</strong>
Автоматизировать полный цикл: оплата → фискализация → обновление CRM → возврат.

<strong>Action:</strong>
<ol>
<li>Выбрал RetailCRM (или Битрикс24) с открытым API для интеграции</li>
<li>Интегрировал платёжный шлюз (CloudPayments/Stripe) через REST API: приём платежей, webhooks для статусов, refund API</li>
<li>Настроил онлайн-кассу (Атол/Эвотор) через API: автоматическая фискализация при подтверждении платежа, чек «возврат прихода» при refund</li>
<li>Разработал middleware-сервис для синхронизации: платёжный шлюз → касса → CRM</li>
<li>Поставил задачи разработчикам: API-интеграции, обработка ошибок, retry logic, логирование</li>
<li>Провёл тестирование: 50 тестовых платежей, 10 возвратов, проверка edge cases (таймаут, дубли, ошибки кассы)</li>
</ol>

<strong>Result:</strong>
<ul>
<li>Время обработки заказа: с 2 часов до 5 минут</li>
<li>Ошибки фискализации: с 15% до <1%</li>
<li>Возвраты: с 3-5 дней до 1 дня (автоматическая инициация через CRM)</li>
<li>Сокращение штата операционистов на 40%</li>
</ul>`,
                            status: 'not-started',
                            difficulty: 4,
                            tips: 'Это «killer answer» для данной позиции. Подготовьте конкретные цифры, названия систем, сроки. Если проект был реальный — отлично. Если нет — подготовьте гипотетический, но максимально детализированный кейс.'
                        }
                    ]
                },
                {
                    id: 'salary',
                    name: 'Вопросы о зарплате и мотивации',
                    icon: '💰',
                    color: '#ff9ff3',
                    questions: [
                        {
                            id: 9,
                            text: 'Какие у вас зарплатные ожидания?',
                            answer: 'Называйте диапазон, основанный на рыночных данных. Укажите, что готовы обсуждать весь пакет.',
                            status: 'not-started',
                            difficulty: 3,
                            tips: 'Исследуйте рынок (levels.fyi, glassdoor, hh.ru). Не называйте число первым, если возможно.'
                        }
                    ]
                }
            ]
        };

        let editingId = null;
        let editingCategoryId = null;

        function init() {
            renderCategories();
            updateOverallProgress();
            populateCategorySelect();
        }

        function renderCategories() {
            const container = document.getElementById('categoriesContainer');
            container.innerHTML = '';

            data.categories.forEach(category => {
                const categoryDiv = document.createElement('div');
                categoryDiv.className = 'category';
                categoryDiv.dataset.categoryId = category.id;

                const total = category.questions.length;
                const learned = category.questions.filter(q => q.status === 'learned' || q.status === 'interview').length;
                const progress = total > 0 ? Math.round((learned / total) * 100) : 0;

                categoryDiv.innerHTML = `
                    <div class="category-header" onclick="toggleCategory('${category.id}')">
                        <div class="category-title">
                            <div class="category-icon" style="background: ${category.color}20; color: ${category.color}">
                                ${category.icon}
                            </div>
                            <h3>${category.name}</h3>
                        </div>
                        <div class="category-progress">
                            <div class="mini-progress">
                                <div class="mini-progress-bar" style="width: ${progress}%"></div>
                            </div>
                            <span style="color: #666; font-size: 0.9rem;">${learned}/${total}</span>
                            <button class="toggle-btn" id="toggle-${category.id}">▼</button>
                        </div>
                    </div>
                    <div class="questions-list" id="list-${category.id}">
                        ${category.questions.map(q => renderQuestion(q, category.id)).join('')}
                        <button class="add-question-btn" onclick="openModal('${category.id}')">➕ Добавить вопрос</button>
                    </div>
                `;

                container.appendChild(categoryDiv);
            });
        }

        function renderQuestion(question, categoryId) {
            const statusLabels = {
                'not-started': 'Не начато',
                'learning': 'В процессе',
                'learned': 'Изучено',
                'interview': 'На собесе'
            };

            const statusClasses = {
                'not-started': 'badge-not-started',
                'learning': 'badge-learning',
                'learned': 'badge-learned',
                'interview': 'badge-interview'
            };

            let difficultyDots = '';
            for (let i = 1; i <= 5; i++) {
                difficultyDots += `<div class="difficulty-dot ${i <= question.difficulty ? 'active' : ''}"></div>`;
            }

            return `
                <div class="question-item ${question.difficulty >= 4 ? 'priority-high' : question.difficulty >= 3 ? 'priority-medium' : 'priority-low'}" data-question-id="${question.id}" data-category-id="${categoryId}">
                    <div class="question-header">
                        <div class="question-text">
                            ${question.text}
                            <span class="difficulty">${difficultyDots}</span>
                        </div>
                        <div class="status-badges">
                            <span class="badge ${statusClasses[question.status]}" onclick="cycleStatus('${categoryId}', ${question.id}, event)">
                                ${statusLabels[question.status]}
                            </span>
                            <span class="badge" style="background: #f0f0f0; color: #666; cursor: pointer;" onclick="editQuestion('${categoryId}', ${question.id}, event)">
                                ✏️
                            </span>
                            <span class="badge" style="background: #ffebee; color: #c62828; cursor: pointer;" onclick="deleteQuestion('${categoryId}', ${question.id}, event)">
                                🗑️
                            </span>
                        </div>
                    </div>
                    ${question.answer ? `
                        <div class="answer-section">
                            <div class="answer-text">${question.answer}</div>
                        </div>
                    ` : ''}
                    ${question.tips ? `
                        <div class="tips-section">
                            <strong>💡 Советы:</strong> ${question.tips}
                        </div>
                    ` : ''}
                </div>
            `;
        }

        function toggleCategory(categoryId) {
            const list = document.getElementById(`list-${categoryId}`);
            const btn = document.getElementById(`toggle-${categoryId}`);
            list.classList.toggle('active');
            btn.classList.toggle('rotated');
        }

        function cycleStatus(categoryId, questionId, event) {
            event.stopPropagation();
            const category = data.categories.find(c => c.id === categoryId);
            const question = category.questions.find(q => q.id === questionId);

            const statuses = ['not-started', 'learning', 'learned', 'interview'];
            const currentIndex = statuses.indexOf(question.status);
            question.status = statuses[(currentIndex + 1) % statuses.length];

            renderCategories();
            updateOverallProgress();
        }

        function updateOverallProgress() {
            let total = 0;
            let learned = 0;
            let inProgress = 0;
            let notStarted = 0;

            data.categories.forEach(cat => {
                cat.questions.forEach(q => {
                    total++;
                    if (q.status === 'learned' || q.status === 'interview') learned++;
                    else if (q.status === 'learning') inProgress++;
                    else notStarted++;
                });
            });

            const progress = total > 0 ? Math.round((learned / total) * 100) : 0;

            document.getElementById('overallBar').style.width = progress + '%';
            document.getElementById('overallBar').textContent = progress + '%';
            document.getElementById('totalQuestions').textContent = total;
            document.getElementById('learnedQuestions').textContent = learned;
            document.getElementById('inProgress').textContent = inProgress;
            document.getElementById('notStarted').textContent = notStarted;
        }

        function openModal(categoryId = null) {
            editingId = null;
            editingCategoryId = null;
            document.getElementById('modalTitle').textContent = 'Добавить вопрос';
            document.getElementById('questionForm').reset();

            if (categoryId) {
                document.getElementById('categorySelect').value = categoryId;
            }

            document.getElementById('questionModal').classList.add('active');
        }

        function closeModal() {
            document.getElementById('questionModal').classList.remove('active');
            editingId = null;
            editingCategoryId = null;
        }

        function populateCategorySelect() {
            const select = document.getElementById('categorySelect');
            select.innerHTML = '<option value="">Выберите категорию</option>';
            data.categories.forEach(cat => {
                select.innerHTML += `<option value="${cat.id}">${cat.name}</option>`;
            });
        }

        function saveQuestion(event) {
            event.preventDefault();

            const categoryId = document.getElementById('categorySelect').value;
            const text = document.getElementById('questionInput').value;
            const answer = document.getElementById('answerInput').value;
            const status = document.getElementById('statusSelect').value;
            const difficulty = parseInt(document.getElementById('difficultySelect').value);
            const tips = document.getElementById('tipsInput').value;

            const category = data.categories.find(c => c.id === categoryId);

            if (editingId && editingCategoryId) {
                const oldCategory = data.categories.find(c => c.id === editingCategoryId);
                const question = oldCategory.questions.find(q => q.id === editingId);
                question.text = text;
                question.answer = answer;
                question.status = status;
                question.difficulty = difficulty;
                question.tips = tips;

                if (oldCategory.id !== categoryId) {
                    oldCategory.questions = oldCategory.questions.filter(q => q.id !== editingId);
                    category.questions.push(question);
                }
            } else {
                const newId = Math.max(...data.categories.flatMap(c => c.questions.map(q => q.id)), 0) + 1;
                category.questions.push({
                    id: newId,
                    text,
                    answer,
                    status,
                    difficulty,
                    tips
                });
            }

            closeModal();
            renderCategories();
            updateOverallProgress();
        }

        function editQuestion(categoryId, questionId, event) {
            event.stopPropagation();
            const category = data.categories.find(c => c.id === categoryId);
            const question = category.questions.find(q => q.id === questionId);

            editingId = questionId;
            editingCategoryId = categoryId;

            document.getElementById('modalTitle').textContent = 'Редактировать вопрос';
            document.getElementById('categorySelect').value = categoryId;
            document.getElementById('questionInput').value = question.text;
            document.getElementById('answerInput').value = question.answer || '';
            document.getElementById('statusSelect').value = question.status;
            document.getElementById('difficultySelect').value = question.difficulty;
            document.getElementById('tipsInput').value = question.tips || '';

            document.getElementById('questionModal').classList.add('active');
        }

        function deleteQuestion(categoryId, questionId, event) {
            event.stopPropagation();
            if (confirm('Удалить этот вопрос?')) {
                const category = data.categories.find(c => c.id === categoryId);
                category.questions = category.questions.filter(q => q.id !== questionId);
                renderCategories();
                updateOverallProgress();
            }
        }

        function searchQuestions() {
            const query = document.getElementById('searchBox').value.toLowerCase();
            const items = document.querySelectorAll('.question-item');

            items.forEach(item => {
                const text = item.querySelector('.question-text').textContent.toLowerCase();
                const answer = item.querySelector('.answer-text')?.textContent.toLowerCase() || '';

                if (text.includes(query) || answer.includes(query)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });

            if (query) {
                document.querySelectorAll('.questions-list').forEach(list => list.classList.add('active'));
                document.querySelectorAll('.toggle-btn').forEach(btn => btn.classList.add('rotated'));
            }
        }

        function exportData() {
            const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'interview-tracker-data.json';
            a.click();
            URL.revokeObjectURL(url);
        }

        function importData(input) {
            const file = input.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = function(e) {
                try {
                    const imported = JSON.parse(e.target.result);
                    if (imported.categories) {
                        data = imported;
                        renderCategories();
                        updateOverallProgress();
                        populateCategorySelect();
                        alert('Данные успешно импортированы!');
                    } else {
                        alert('Неверный формат файла');
                    }
                } catch (err) {
                    alert('Ошибка при чтении файла');
                }
            };
            reader.readAsText(file);
            input.value = '';
        }

        document.getElementById('questionModal').addEventListener('click', function(e) {
            if (e.target === this) closeModal();
        });

        init();
    </script>
</body>
</html>
