// Список URL для аудита

const urlList: string[] = [
    "https://site.com/page-1",
    "https://site.com/page-2",
    "https://site.com/page-3"
];

console.log("Всего URL: " + urlList.length);

// Перебираем каждый URL
for (let i = 0; i < urlList.length; i++) {
    console.log(`${i + 1}. Проверяем: ${urlList[i]}`);
}

// Добавить новый URL
urlList.push("https://site.com/page-4");
console.log("Теперь URL: " + urlList.length);
