// Объект — карточка страницы для SEO-аудита

const page = {
    url: "https://shop.com/iphone-15",
    title: "Купить iPhone 15 в Москве",
    h1: "iPhone 15",
    description: "Лучшие цены на iPhone 15",
    isIndexed: true
};

console.log("URL: " + page.url);
console.log("Title: " + page.title);

// Проверка: Title не должен быть длиннее 60 символов
if (page.title.length > 60) {
    console.log("⚠️ Title слишком длинный!");
} else {
    console.log("✅ Title в порядке");
}
