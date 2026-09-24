import { RawLexiconItem } from './types';
import { getMongolianVowelHarmony, generateApproximateIPA } from './phonologyUtils';

// Curated seed groups across all CEFR levels & domains
interface WordSeed {
  m: string; // Cyrillic
  e: string; // English
  pos: RawLexiconItem['pos'];
  cefr: RawLexiconItem['cefr'];
  cat: string;
  exM: string; // Example Mongolian
  exE: string; // Example English
}

const SEEDS_A1: WordSeed[] = [
  // Alphabet & Phonology basics
  { m: 'эгшиг', e: 'vowel', pos: 'noun', cefr: 'A1', cat: 'Phonology', exM: 'Монгол хэлэнд эр, эм эгшиг бий.', exE: 'In Mongolian there are masculine and feminine vowels.' },
  { m: 'гийгүүлэгч', e: 'consonant', pos: 'noun', cefr: 'A1', cat: 'Phonology', exM: 'Энэ үг гурван гийгүүлэгчтэй.', exE: 'This word has three consonants.' },
  { m: 'үсэг', e: 'letter, alphabet character', pos: 'noun', cefr: 'A1', cat: 'Phonology', exM: 'Монгол кирилл цагаан толгой 35 үсэгтэй.', exE: 'The Mongolian Cyrillic alphabet has 35 letters.' },
  { m: 'үг', e: 'word', pos: 'noun', cefr: 'A1', cat: 'Phonology', exM: 'Шинэ үг цээжлэх хэрэгтэй.', exE: 'Need to memorize new words.' },
  { m: 'өгүүлбэр', e: 'sentence', pos: 'noun', cefr: 'A1', cat: 'Phonology', exM: 'Энэ өгүүлбэрийг уншаарай.', exE: 'Please read this sentence.' },
  
  // Greetings & Social Courtesy
  { m: 'сайн байна уу', e: 'hello, how are you (polite)', pos: 'interjection', cefr: 'A1', cat: 'Greetings', exM: 'Сайн байна уу, багш аа?', exE: 'Hello, teacher?' },
  { m: 'сайн', e: 'good, well', pos: 'adjective', cefr: 'A1', cat: 'Greetings', exM: 'Би сайн байна.', exE: 'I am doing well.' },
  { m: 'баярлалаа', e: 'thank you', pos: 'interjection', cefr: 'A1', cat: 'Greetings', exM: 'Маш их баярлалаа.', exE: 'Thank you very much.' },
  { m: 'баяртай', e: 'goodbye', pos: 'interjection', cefr: 'A1', cat: 'Greetings', exM: 'Маргааш уулзъя, баяртай!', exE: 'See you tomorrow, goodbye!' },
  { m: 'тийм', e: 'yes', pos: 'particle', cefr: 'A1', cat: 'Greetings', exM: 'Тийм, би ойлгосон.', exE: 'Yes, I understood.' },
  { m: 'үгүй', e: 'no', pos: 'particle', cefr: 'A1', cat: 'Greetings', exM: 'Үгүй, би монгол биш.', exE: 'No, I am not Mongolian.' },
  { m: 'уучлаарай', e: 'excuse me, sorry', pos: 'interjection', cefr: 'A1', cat: 'Greetings', exM: 'Уучлаарай, би хоцорчихлоо.', exE: 'Excuse me, I am late.' },
  { m: 'зүгээр', e: 'it is okay, no problem', pos: 'adverb', cefr: 'A1', cat: 'Greetings', exM: 'Зүгээр ээ, санаа зоволтгүй.', exE: 'It is fine, do not worry.' },
  { m: 'тавтай морил', e: 'welcome', pos: 'interjection', cefr: 'A1', cat: 'Greetings', exM: 'Манай гэрт тавтай морилно уу.', exE: 'Welcome to our home.' },

  // Pronouns
  { m: 'би', e: 'I', pos: 'pronoun', cefr: 'A1', cat: 'Pronouns', exM: 'Би оюутан.', exE: 'I am a student.' },
  { m: 'чи', e: 'you (informal, singular)', pos: 'pronoun', cefr: 'A1', cat: 'Pronouns', exM: 'Чи хаанаас ирсэн бэ?', exE: 'Where did you come from?' },
  { m: 'та', e: 'you (polite/honorific, or plural)', pos: 'pronoun', cefr: 'A1', cat: 'Pronouns', exM: 'Та ямар ажил хийдэг вэ?', exE: 'What work do you do?' },
  { m: 'тэр', e: 'he, she, it, that', pos: 'pronoun', cefr: 'A1', cat: 'Pronouns', exM: 'Тэр хүн хэн бэ?', exE: 'Who is that person?' },
  { m: 'бид', e: 'we (exclusive/general)', pos: 'pronoun', cefr: 'A1', cat: 'Pronouns', exM: 'Бид монгол хэл сурч байна.', exE: 'We are learning Mongolian.' },
  { m: 'бид нар', e: 'we (plural explicit)', pos: 'pronoun', cefr: 'A1', cat: 'Pronouns', exM: 'Бид нар номын санд байна.', exE: 'We are at the library.' },
  { m: 'та нар', e: 'you all (plural)', pos: 'pronoun', cefr: 'A1', cat: 'Pronouns', exM: 'Та нар цай уух уу?', exE: 'Will you all drink tea?' },
  { m: 'тэд', e: 'they', pos: 'pronoun', cefr: 'A1', cat: 'Pronouns', exM: 'Тэд Улаанбаатарт амьдардаг.', exE: 'They live in Ulaanbaatar.' },
  { m: 'энэ', e: 'this', pos: 'pronoun', cefr: 'A1', cat: 'Pronouns', exM: 'Энэ юу вэ?', exE: 'What is this?' },
  { m: 'тэр', e: 'that (visible)', pos: 'pronoun', cefr: 'A1', cat: 'Pronouns', exM: 'Тэр ном минийх.', exE: 'That book is mine.' },

  // Numbers 0-20, 30, 40, 50, 100, 1000
  { m: 'тэг', e: 'zero', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Тэг градус байна.', exE: 'It is zero degrees.' },
  { m: 'нэг', e: 'one', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Нэг аяга цай авъя.', exE: 'I will take one cup of tea.' },
  { m: 'хоёр', e: 'two', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Хоёр хүүхэд тоглож байна.', exE: 'Two children are playing.' },
  { m: 'гурав', e: 'three', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Гурав хоногийн дараа уулзъя.', exE: 'See you in three days.' },
  { m: 'дөрөв', e: 'four', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Манайд дөрвөн өрөө бий.', exE: 'Our place has four rooms.' },
  { m: 'тав', e: 'five', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Таван хошуу мал.', exE: 'The five kinds of livestock.' },
  { m: 'зургаа', e: 'six', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Зургаан цаг болж байна.', exE: 'It is six o\'clock.' },
  { m: 'долоо', e: 'seven', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Долоо хоногт долоон өдөр бий.', exE: 'In a week there are seven days.' },
  { m: 'найм', e: 'eight', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Найман сард дулаахан.', exE: 'It is warm in August.' },
  { m: 'ес', e: 'nine', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Есөн эрдэнэ.', exE: 'The nine precious gems.' },
  { m: 'арав', e: 'ten', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Арван минут хүлээгээрэй.', exE: 'Please wait ten minutes.' },
  { m: 'хорь', e: 'twenty', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Хорин төгрөг.', exE: 'Twenty tugriks.' },
  { m: 'гуч', e: 'thirty', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Гучин настай.', exE: 'Thirty years old.' },
  { m: 'дөч', e: 'forty', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Дөчин хувь.', exE: 'Forty percent.' },
  { m: 'тавь', e: 'fifty', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Тавин километр.', exE: 'Fifty kilometers.' },
  { m: 'жар', e: 'sixty', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Жаран жил.', exE: 'Sixty years.' },
  { m: 'дал', e: 'seventy', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Далан настай өвөө.', exE: 'Seventy year old grandfather.' },
  { m: 'ная', e: 'eighty', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Наян хуудас ном.', exE: 'An eighty page book.' },
  { m: 'ер', e: 'ninety', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Ерийн хувьтай тэнцэнэ.', exE: 'Equals ninety percent.' },
  { m: 'зуу', e: 'hundred', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Зуун төгрөг өгье.', exE: 'I will give one hundred tugriks.' },
  { m: 'мянга', e: 'thousand', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Мянган жилийн түүх.', exE: 'A thousand year history.' },
  { m: 'түм', e: 'ten thousand, myriad', pos: 'numeral', cefr: 'A1', cat: 'Numbers', exM: 'Түмэн олон хүн.', exE: 'Ten thousand crowds of people.' },

  // Family & People
  { m: 'аав', e: 'father', pos: 'noun', cefr: 'A1', cat: 'Family', exM: 'Миний аав багш.', exE: 'My father is a teacher.' },
  { m: 'ээж', e: 'mother', pos: 'noun', cefr: 'A1', cat: 'Family', exM: 'Ээж цай чанаж байна.', exE: 'Mother is brewing tea.' },
  { m: 'ах', e: 'older brother', pos: 'noun', cefr: 'A1', cat: 'Family', exM: 'Миний ах их сургуульд сурдаг.', exE: 'My older brother studies at university.' },
  { m: 'эгч', e: 'older sister', pos: 'noun', cefr: 'A1', cat: 'Family', exM: 'Эгч эмнэлэгт ажилладаг.', exE: 'Older sister works in a hospital.' },
  { m: 'дүү', e: 'younger sibling', pos: 'noun', cefr: 'A1', cat: 'Family', exM: 'Эрэгтэй дүү сургуульд явлаа.', exE: 'Younger brother went to school.' },
  { m: 'эмээ', e: 'grandmother', pos: 'noun', cefr: 'A1', cat: 'Family', exM: 'Эмээ үлгэр ярьж өгөв.', exE: 'Grandmother told a tale.' },
  { m: 'өвөө', e: 'grandfather', pos: 'noun', cefr: 'A1', cat: 'Family', exM: 'Өвөө морь унах дуртай.', exE: 'Grandfather likes to ride horses.' },
  { m: 'хүү', e: 'son, boy', pos: 'noun', cefr: 'A1', cat: 'Family', exM: 'Түүний хүү ухаантай.', exE: 'His son is smart.' },
  { m: 'охин', e: 'daughter, girl', pos: 'noun', cefr: 'A1', cat: 'Family', exM: 'Энэ охин дуу сайн дуулдаг.', exE: 'This girl sings well.' },
  { m: 'хүүхэд', e: 'child, children', pos: 'noun', cefr: 'A1', cat: 'Family', exM: 'Хүүхдүүд гадаа тоглож байна.', exE: 'Children are playing outside.' },
  { m: 'найз', e: 'friend', pos: 'noun', cefr: 'A1', cat: 'Family', exM: 'Миний сайн найз Бат.', exE: 'My good friend is Bat.' },
  { m: 'хүн', e: 'person, human', pos: 'noun', cefr: 'A1', cat: 'People', exM: 'Монгол хүн найрсаг.', exE: 'Mongolian people are hospitable.' },
  { m: 'багш', e: 'teacher', pos: 'noun', cefr: 'A1', cat: 'People', exM: 'Багш самбар дээр бичиж байна.', exE: 'The teacher is writing on the blackboard.' },
  { m: 'оюутан', e: 'student', pos: 'noun', cefr: 'A1', cat: 'People', exM: 'Тэр оюутан шалгалт өгсөн.', exE: 'That student took an exam.' },

  // Basic Verbs
  { m: 'байх', e: 'to be, to exist', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Би энд байна.', exE: 'I am here.' },
  { m: 'хийх', e: 'to do, to make', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Чи юу хийж байна вэ?', exE: 'What are you doing?' },
  { m: 'явах', e: 'to go', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Би харьж явна.', exE: 'I am going home.' },
  { m: 'ирэх', e: 'to come', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Манай найз маргааш ирнэ.', exE: 'My friend will come tomorrow.' },
  { m: 'үзэх', e: 'to see, to watch', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Бид кино үзлээ.', exE: 'We watched a movie.' },
  { m: 'унших', e: 'to read', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Энэ номыг уншаарай.', exE: 'Please read this book.' },
  { m: 'бичих', e: 'to write', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Захиа бичих дуртай.', exE: 'I like to write letters.' },
  { m: 'идэх', e: 'to eat', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Өглөөний цайгаа идсэн үү?', exE: 'Did you eat your breakfast?' },
  { m: 'уух', e: 'to drink', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Халуун цай ууя.', exE: 'Let us drink hot tea.' },
  { m: 'ярих', e: 'to speak, to talk', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Тэр монголоор сайн ярьдаг.', exE: 'He speaks Mongolian well.' },
  { m: 'сонсох', e: 'to listen, to hear', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Радио сонсож байна.', exE: 'Listening to the radio.' },
  { m: 'авах', e: 'to take, to buy, to receive', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Талх авъя.', exE: 'I will buy bread.' },
  { m: 'өгөх', e: 'to give', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Надад үзэг өгөөч.', exE: 'Please give me a pen.' },
  { m: 'сурах', e: 'to learn, to study', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Би монгол хэл сурч байна.', exE: 'I am learning Mongolian.' },
  { m: 'мэдэх', e: 'to know', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Би энэ үгийг мэднэ.', exE: 'I know this word.' },
  { m: 'ойлголоо', e: 'understood', pos: 'verb', cefr: 'A1', cat: 'Verbs', exM: 'Би бүгдийг ойлголоо.', exE: 'I understood everything.' }
];

export { SEEDS_A1 };
