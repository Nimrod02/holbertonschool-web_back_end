function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw error('Cannot process');
  }

  for (const [key] of map) {
    if (map.get(key) === 1) map.set(key, 1000);
  }
  return map;
}
export default updateUniqueItems;
