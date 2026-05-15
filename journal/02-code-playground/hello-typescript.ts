// Это моя первая программа на TypeScript

// Переменная — это коробка с надписью
let myName: string = "Камиль";
let myAge: number = 21;
let isLearning: boolean = true;

// Выводим в консоль
console.log("Привет, меня зовут " + myName);
console.log("Мне " + myAge + " лет");
console.log("Я учу TypeScript: " + isLearning);

// Функция — это рецепт
function greet(name: string): string {
    return "Привет, " + name + "!";
}

console.log(greet("Мир"));
