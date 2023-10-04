export default function getStudentIdsSum(students, id) {
  return students.reduce((accumulator, student) => accumulator + student.id, 0);
}
