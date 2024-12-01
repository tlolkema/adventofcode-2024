const input = await Deno.readTextFile("./day-1/input-full.txt");
const lines = input.split("\n");

const left = lines
  .map((line) => line.split("   ")[0])
  .sort((a, b) => Number(a) - Number(b));

const right = lines
  .map((line) => line.split("   ")[1])
  .sort((a, b) => Number(a) - Number(b));

const diffTotal = left.reduce((total, item, index) => {
  const diff = Math.abs(Number(item) - Number(right[index]));
  return total + diff;
}, 0);

console.log(diffTotal);
