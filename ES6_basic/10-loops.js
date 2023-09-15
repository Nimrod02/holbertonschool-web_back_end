export default function appendToEachArrayValue(array, appendring) {
  const myarray = [];
  for (const idx of array) {
    myarray.push(appendring + idx);
  }

  return myarray;
}
