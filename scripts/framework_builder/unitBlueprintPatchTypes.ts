import { UnitSpec } from './unitTypes';

export interface UnitDataSpec {
  title: string;
  theme: string;
  primaryPurpose: string;
  primaryComp: string;
  secondaryComp?: string;
  gramIntro: string[];
  gramReinforced: string[];
  phonoTargets: string[];
  comm: string[];
  dom: string[];
  coreLemmas: number;
  domainLemmas: number;
  generalLemmas: number;
  expressions: number;
  readingGenre: string;
  readingLength: string;
  readingSkills: string[];
  listeningGenre: string;
  listeningRate: string;
  listeningSuitability: "standard_speech_synthesis" | "mongolian_speech_synthesis_only" | "native_speaker_preferred";
  listeningSkills: string[];
  writingGenre: string;
  writingLength: string;
  writingSkills: string[];
  spokenGenre: string;
  spokenTask: string;
  spokenSkills: string[];
  register: string;
  cultureTitle: string;
  cultureScope: string;
  cultureDetails: string;
  prereqs: number[]; // sequence positions of prerequisite units
  reviews: number[]; // sequence positions of reviewed units
  futureHints: string[];
  outcome: string;
}
