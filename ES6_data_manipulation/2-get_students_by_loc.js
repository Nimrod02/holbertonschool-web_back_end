export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }

  const filteredStudents = students.filter((student) => student.location === city);
  return filteredStudents;
}
