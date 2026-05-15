// Простой калькулятор для SEO-метрик

function calculateCTR(clicks: number, impressions: number): number {
    return (clicks / impressions) * 100;
}

// Пример: 150 кликов из 3000 показов
const clicks: number = 150;
const impressions: number = 3000;
const ctr: number = calculateCTR(clicks, impressions);

console.log(`CTR = ${ctr.toFixed(2)}%`);
// toFixed(2) — округлить до 2 знаков после запятой

// Ещё пример: посчитать стоимость клика
function calculateCPC(cost: number, clicks: number): number {
    return cost / clicks;
}

const cpc = calculateCPC(5000, 150); // 5000 рублей, 150 кликов
console.log(`CPC = ${cpc.toFixed(2)} руб.`);
