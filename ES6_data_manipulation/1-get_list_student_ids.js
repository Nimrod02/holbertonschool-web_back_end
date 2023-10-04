export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const data = students.map((obj) => obj.id);
  return data;
}
