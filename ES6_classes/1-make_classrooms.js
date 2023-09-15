import ClassRoom from "./0-classroom.js";

export default function initializeRooms() {
  const classroom_1 = new ClassRoom(19);
  const classroom_2 = new ClassRoom(20);
  const classroom_3 = new ClassRoom(34);

  return [classroom_1, classroom_2, classroom_3];
}
