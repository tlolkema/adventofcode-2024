const input = await Deno.readTextFile("./day-1/input-full.txt");
const lines = input.split("\n");

const left = lines
  .map((line) => line.split("   ")[0])
  .sort((a, b) => Number(a) - Number(b));

const right = lines
  .map((line) => line.split("   ")[1])
  .sort((a, b) => Number(a) - Number(b));

const count = (arr: string[], item: string) => {
  return arr.filter((leftItem) => leftItem === item).length;
};

const similarityScore = left.reduce((total, item) => {
  const score = Math.abs(Number(item) * count(right, item));
  return total + score;
}, 0);

console.log(similarityScore);
