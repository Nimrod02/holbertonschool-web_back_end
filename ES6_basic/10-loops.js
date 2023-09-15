export default function appendToEachArrayValue(array) {
  for (const idx of array) {
    array[idx];
  }

  return array;
}
