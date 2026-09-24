import { preA1_Units_01_to_03, preA1_Units_04_to_07 } from "./dataPilotPreA1_Part1";
import { preA1_Units_08_to_11 } from "./dataPilotPreA1_Part2";
import { preA1_Units_12_to_15 } from "./dataPilotPreA1_Part3";
import { a1_Units_16_to_19 } from "./dataPilotA1_Part1";
import { a1_Units_20_to_23 } from "./dataPilotA1_Part2";
import { LessonBlueprint } from "./lessonBlueprintTypes";

export const allPilotLessons: LessonBlueprint[] = [
  ...preA1_Units_01_to_03,
  ...preA1_Units_04_to_07,
  ...preA1_Units_08_to_11,
  ...preA1_Units_12_to_15,
  ...a1_Units_16_to_19,
  ...a1_Units_20_to_23
];

console.log("Total Pilot Lessons compiled:", allPilotLessons.length);
