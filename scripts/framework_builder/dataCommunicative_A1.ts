export interface CommunicativeFunctionSpec {
  functionId: string;
  title: string;
  mongolianTitle: string;
  level: string;
  domain: string;
  prerequisites: string[];
  communicativeGoal: string;
  typicalScenarios: string[];
  keyStructures: string[];
  expectedOutcome: string;
}

export const communicativeA1Data: CommunicativeFunctionSpec[] = [
  // Pre-A1 / A1 Entry & Survival Functions
  {
    functionId: "comm_a1_01_formulaic_greetings",
    title: "Exchange Everyday Formulaic Greetings",
    mongolianTitle: "Өдөр тутмын мэндчилгээ солилцох",
    level: "A1",
    domain: "Interpersonal",
    prerequisites: [],
    communicativeGoal: "Greet peers and acquaintances casually and inquire about well-being using basic conversational formulas.",
    typicalScenarios: ["Passing a classmate in hallway", "Entering a small neighborhood shop", "Greeting colleagues in the morning"],
    keyStructures: ["Сайн байна уу?", "Сайн, та сайн байна уу?", "Өглөөний мэнд", "Өдрийн мэнд", "Оройн мэнд"],
    expectedOutcome: "Learner greets others promptly with natural rhythm and appropriate reciprocal responses."
  },
  {
    functionId: "comm_a1_02_formal_elder_greetings",
    title: "Respectfully Greet Elders and Dignitaries",
    mongolianTitle: "Ахмад настан, хүндэт хүмүүстэй ёслон мэндлэх",
    level: "A1",
    domain: "Interpersonal",
    prerequisites: ["comm_a1_01_formulaic_greetings"],
    communicativeGoal: "Greet senior individuals using honorific posture and traditional well-being inquiries.",
    typicalScenarios: ["Meeting a host grandmother", "Visiting a professor's office", "Arriving at a countryside home"],
    keyStructures: ["Та амархан сайн байна уу?", "Та бие лагшин тунгалаг уу?", "Амар мэнд үү?"],
    expectedOutcome: "Learner demonstrates respect using appropriate honorary phrasing and bodily comportment."
  },
  {
    functionId: "comm_a1_03_departures_farewells",
    title: "Parting, Leave-Taking, and Future Promises",
    mongolianTitle: "Салж одох ба үдэх үг хэллэг хэрэглэх",
    level: "A1",
    domain: "Interpersonal",
    prerequisites: ["comm_a1_01_formulaic_greetings"],
    communicativeGoal: "Take leave in casual and formal contexts and indicate when next contact will occur.",
    typicalScenarios: ["Leaving a party", "Ending a lesson", "Saying goodbye at the bus stop"],
    keyStructures: ["Баяртай", "Маргааш уулзъя", "Дараа тухтай уулзъя", "Сайн яваарай", "Сайн сууж байгаарай"],
    expectedOutcome: "Learner distinguishes between parting words for the person departing vs the person remaining."
  },
  {
    functionId: "comm_a1_04_expressing_gratitude",
    title: "Express Gratitude and Acknowledge Thanks",
    mongolianTitle: "Талархал илэрхийлэх ба хариу хэлэх",
    level: "A1",
    domain: "Interpersonal",
    prerequisites: ["comm_a1_01_formulaic_greetings"],
    communicativeGoal: "Offer sincere thanks for assistance, gifts, or hospitality, and respond gracefully.",
    typicalScenarios: ["Receiving change or food", "Being offered tea", "Accepting directions from a stranger"],
    keyStructures: ["Баярлалаа", "Их баярлалаа", "Гялайлаа", "Зүгээр ээ", "Зүгээр зүгээр"],
    expectedOutcome: "Learner selects appropriate gratitude intensity and delivers quick polite acknowledgments."
  },
  {
    functionId: "comm_a1_05_apologies_pardon",
    title: "Apologize, Excuse Oneself, and Request Pardon",
    mongolianTitle: "Хүлцэл өчих, уучлалт гуйх",
    level: "A1",
    domain: "Interpersonal",
    prerequisites: ["comm_a1_01_formulaic_greetings"],
    communicativeGoal: "Apologize for small accidents, get someone's attention, or ask someone to make way.",
    typicalScenarios: ["Bumping someone on a crowded bus", "Arriving slightly late", "Interrupting to ask a question"],
    keyStructures: ["Уучлаарай", "Өршөөгөөрэй", "Харамсалтай байна", "Зүгээр, зүгээр"],
    expectedOutcome: "Learner employs polite excuse formulas naturally in crowded or unexpected situations."
  },
  {
    functionId: "comm_a1_06_self_introduction_name",
    title: "State One's Name and Inquire Interlocutor's Name",
    mongolianTitle: "Өөрийн нэрийг хэлэх ба бусдын нэрийг асуух",
    level: "A1",
    domain: "Interpersonal",
    prerequisites: ["comm_a1_01_formulaic_greetings"],
    communicativeGoal: "State full name, preferred nickname, and ask someone's name respectfully.",
    typicalScenarios: ["First day of language class", "Meeting roommates", "Introducing oneself to a colleague"],
    keyStructures: ["Намайг ... гэдэг", "Миний нэрийг ... гэдэг", "Таны нэр хэн бэ?", "Чамайг хэн гэдэг вэ?"],
    expectedOutcome: "Learner introduces self accurately and asks peer or elder's name with correct register."
  },
  {
    functionId: "comm_a1_07_origin_nationality",
    title: "State Country of Origin, Nationality, and Hometown",
    mongolianTitle: "Улс үндэстэн, төрсөн нутаг, харьяаллаа илэрхийлэх",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_06_self_introduction_name"],
    communicativeGoal: "Declare citizenship, country of origin, and birthplace, and ask where others are from.",
    typicalScenarios: ["Passport control / registration", "Conversation with taxi driver", "Social gathering"],
    keyStructures: ["Би Америк / Герман / Япон хүн", "Би Улаанбаатараас ирсэн", "Та хаанаас ирсэн бэ?", "Танай нутаг хаана вэ?"],
    expectedOutcome: "Learner states nationality with correct demonym and ablative origin construction."
  },
  {
    functionId: "comm_a1_08_professions_occupations",
    title: "Identify Profession, Job, or Student Status",
    mongolianTitle: "Мэргэжил, эрхэлж буй ажил, сургуулиа танилцуулах",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_06_self_introduction_name"],
    communicativeGoal: "State one's line of work or study and ask others about their occupation.",
    typicalScenarios: ["Networking event", "Visa interview", "Casual dinner conversation"],
    keyStructures: ["Би оюутан / багш / эмч / инженер", "Би их сургуульд сурдаг", "Та ямар ажил хийдэг вэ?"],
    expectedOutcome: "Learner describes occupation using nominative profession terms without artificial copulas."
  },
  {
    functionId: "comm_a1_09_introducing_others",
    title: "Introduce Friends, Colleagues, and Companions",
    mongolianTitle: "Найз нөхөд, хамт олноо танилцуулах",
    level: "A1",
    domain: "Interpersonal",
    prerequisites: ["comm_a1_06_self_introduction_name"],
    communicativeGoal: "Present a third party to a group or individual and explain their relationship.",
    typicalScenarios: ["Introducing friend to a host family", "Introducing a colleague at a conference"],
    keyStructures: ["Энэ бол миний найз", "Танилцаарай, энэ манай ажлын хүн", "Танилцсандаа таатай байна"],
    expectedOutcome: "Learner initiates mutual introductions politely using standard demonstrative formulas."
  },
  {
    functionId: "comm_a1_10_identifying_objects",
    title: "Identify Everyday Objects and Inquire About Items",
    mongolianTitle: "Эд зүйлсийг нэрлэх, лавлах",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_01_formulaic_greetings"],
    communicativeGoal: "Point to objects, name common items, and ask what unfamiliar things are called.",
    typicalScenarios: ["Classroom vocabulary building", "Examining items on a desk", "Walking through a shop"],
    keyStructures: ["Энэ юу вэ?", "Тэр юу вэ?", "Энэ бол дэвтэр", "Үүнийг монголоор юу гэдэг вэ?"],
    expectedOutcome: "Learner identifies everyday objects and elicits target language names using demonstratives."
  },
  {
    functionId: "comm_a1_11_ownership_possession",
    title: "Ask and State Ownership of Personal Belongings",
    mongolianTitle: "Эд зүйлийн эзэмшил, хамаарлыг асууж тодруулах",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_10_identifying_objects"],
    communicativeGoal: "Inquire whose item something is and assert or disclaim personal ownership.",
    typicalScenarios: ["Finding lost gloves or keys", "Clarifying belongings in a shared room"],
    keyStructures: ["Энэ хэний цүнх вэ?", "Энэ миний ном", "Тэр таных уу?", "Үгүй ээ, энэ минийх биш"],
    expectedOutcome: "Learner uses genitive forms and possessive pronouns accurately to establish ownership."
  },
  {
    functionId: "comm_a1_12_location_simple_objects",
    title: "Ask and Describe Spatial Location of Objects",
    mongolianTitle: "Эд зүйлийн байршил, орон байрыг заах",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_10_identifying_objects"],
    communicativeGoal: "Ask where an object is and locate it using basic postpositions.",
    typicalScenarios: ["Looking for a pen or phone", "Arranging study desk", "Locating items in a room"],
    keyStructures: ["Миний түлхүүр хаана байна вэ?", "Ширээн дээр байна", "Цүнх дотор байна", "Сандал доор байна"],
    expectedOutcome: "Learner states object coordinates using dative-locative and common spatial postpositions."
  },
  {
    functionId: "comm_a1_13_numbers_counting_1_to_100",
    title: "Count Items and Express Quantities (1 to 100)",
    mongolianTitle: "Нэгээс зуу хүртэл тоолох, тоо ширхэг заах",
    level: "A1",
    domain: "Transactional",
    prerequisites: [],
    communicativeGoal: "Count physical items, recite numbers, and state quantities up to one hundred.",
    typicalScenarios: ["Counting books or chairs", "Stating age", "Specifying quantity when purchasing"],
    keyStructures: ["Нэг, хоёр, гурав, дөрөв, тав", "Арван таван оюутан", "Хэдэн ширхэг вэ?", "Гурав байна"],
    expectedOutcome: "Learner pronounces cardinal numbers correctly and applies them directly before nouns."
  },
  {
    functionId: "comm_a1_14_phone_numbers_contact",
    title: "Exchange Phone Numbers and Contact Information",
    mongolianTitle: "Утасны дугаар, холбоо барих мэдээлэл солилцох",
    level: "A1",
    domain: "Transactional",
    prerequisites: ["comm_a1_13_numbers_counting_1_to_100"],
    communicativeGoal: "Dictate one's phone number digit-by-digit or in pairs, and record another's contact.",
    typicalScenarios: ["Registering for a SIM card", "Exchanging numbers with a new friend", "Booking a cab"],
    keyStructures: ["Таны утасны дугаар хэд вэ?", "Миний дугаар 9911-...", "Дахиад хэлнэ үү", "Би бичээд авлаа"],
    expectedOutcome: "Learner reads and transcribes 8-digit Mongolian telephone numbers without error."
  },
  {
    functionId: "comm_a1_15_family_nuclear_members",
    title: "Identify Immediate Family Members",
    mongolianTitle: "Гэр бүлийн ойрын гишүүдээ нэрлэх",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_06_self_introduction_name"],
    communicativeGoal: "Name parents, siblings, spouse, and children, and describe their basic attributes.",
    typicalScenarios: ["Looking at family photos with a host", "Answering social questions about home"],
    keyStructures: ["Миний аав, ээж", "Надад нэг ах, хоёр дүү бий", "Энэ миний дүү охин"],
    expectedOutcome: "Learner accurately uses Mongolian kinship terms differentiating older vs younger siblings."
  },
  {
    functionId: "comm_a1_16_family_size_marital_status",
    title: "State Family Size and Marital Status",
    mongolianTitle: "Гэр бүлийн бүрэлдэхүүн, ам бүлийн тоо хэлэх",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_15_family_nuclear_members", "comm_a1_13_numbers_counting_1_to_100"],
    communicativeGoal: "State how many people are in one's household and indicate marital status simply.",
    typicalScenarios: ["Completing a census questionnaire", "Conversing with an elder host"],
    keyStructures: ["Манай ам бүл дөрвүүлээ", "Би эхнэртэй / нөхөртэй", "Та хэдэн хүүхэдтэй вэ?", "Би хоёр хүүхэдтэй"],
    expectedOutcome: "Learner expresses collective family counts using collective numeral forms (-уулаа)."
  },
  {
    functionId: "comm_a1_17_ordering_basic_food",
    title: "Order Traditional Staples at a Mongolian Eatery",
    mongolianTitle: "Цайны газарт үндэсний хоол захиалах",
    level: "A1",
    domain: "Transactional",
    prerequisites: ["comm_a1_01_formulaic_greetings", "comm_a1_13_numbers_counting_1_to_100"],
    communicativeGoal: "Order buuz, khuushuur, tsuivan, and other canteen classics with quantities.",
    typicalScenarios: ["Local canteen (цайны газар)", "Roadside food stop in the countryside", "University cafeteria"],
    keyStructures: ["Таван хуушуур авъя", "Нэг аяга цуйван өгөөч", "Бууз байна уу?", "Энд идэх үү, авч явах уу?"],
    expectedOutcome: "Learner places a clear food order specifying quantity and takeaway preference."
  },
  {
    functionId: "comm_a1_18_ordering_drinks_tea",
    title: "Order Beverages and Traditional Milk Tea",
    mongolianTitle: "Уух зүйл, сүүтэй цай захиалах",
    level: "A1",
    domain: "Transactional",
    prerequisites: ["comm_a1_17_ordering_basic_food"],
    communicativeGoal: "Order milk tea, black tea, boiled water, and soft drinks with temperature preferences.",
    typicalScenarios: ["Ordering tea with a meal", "Requesting water in a cafe"],
    keyStructures: ["Сүүтэй цай авъя", "Халуун ус байна уу?", "Нэг аяга хар кофе", "Хүйтэн ус өгөөч"],
    expectedOutcome: "Learner specifies hot vs cold drinks and orders traditional salted milk tea naturally."
  },
  {
    functionId: "comm_a1_19_inquiring_food_ingredients",
    title: "Inquire About Food Ingredients and Meat Types",
    mongolianTitle: "Хоолны орц, махны төрлийг асууж лавлах",
    level: "A1",
    domain: "Transactional",
    prerequisites: ["comm_a1_17_ordering_basic_food"],
    communicativeGoal: "Ask whether a dish contains mutton, beef, pork, or onions, and state dietary limits.",
    typicalScenarios: ["Confirming meat type at a restaurant", "Inquiring about vegetarian options"],
    keyStructures: ["Энэ ямар махтай вэ?", "Хонины махтай юу, үхрийн махтай юу?", "Махгүй хоол байна уу?", "Би мах иддэггүй"],
    expectedOutcome: "Learner verifies meat contents and expresses dietary restrictions unambiguously."
  },
  {
    functionId: "comm_a1_20_asking_bill_payment",
    title: "Ask for the Bill and Execute Cash/Card Payment",
    mongolianTitle: "Тооцоо хийх, үнэ асууж төлбөр төлөх",
    level: "A1",
    domain: "Transactional",
    prerequisites: ["comm_a1_17_ordering_basic_food"],
    communicativeGoal: "Request the total bill, ask about payment methods, and settle payment.",
    typicalScenarios: ["Finishing lunch at a canteen", "Paying a bill in a coffee shop"],
    keyStructures: ["Тооцоо хийе", "Нийт хэдэн төгрөг болсон бэ?", "Картаар төлж болох уу?", "Бэлнээр өгье", "Баримт авъя"],
    expectedOutcome: "Learner signals completion of meal, confirms total, and selects payment instrument."
  },
  {
    functionId: "comm_a1_21_grocery_market_quantities",
    title: "Purchase Groceries by Weight and Unit",
    mongolianTitle: "Хүнсний дэлгүүрт жин ба ширхэгээр худалдаа хийх",
    level: "A1",
    domain: "Transactional",
    prerequisites: ["comm_a1_13_numbers_counting_1_to_100", "comm_a1_20_asking_bill_payment"],
    communicativeGoal: "Request specific weights of meat, flour, or vegetables, and packaged goods.",
    typicalScenarios: ["Neighborhood grocery store", "Open market meat stall", "Bakery kiosk"],
    keyStructures: ["Нэг килограмм мах авъя", "Хоёр ширхэг талх өгөөч", "Энэ ямар үнэтэй вэ?", "Өөр юу авах вэ?"],
    expectedOutcome: "Learner combines numerals, unit classifiers, and nouns to purchase staple foods."
  },
  {
    functionId: "comm_a1_22_shopping_clothing_sizes",
    title: "Inquire About Clothing Sizes and Fitting",
    mongolianTitle: "Хувцасны хэмжээ, өнгө асууж тодруулах",
    level: "A1",
    domain: "Transactional",
    prerequisites: ["comm_a1_10_identifying_objects", "comm_a1_20_asking_bill_payment"],
    communicativeGoal: "Ask for smaller/larger sizes, color variations, and permission to try garments on.",
    typicalScenarios: ["Department store", "Traditional deel workshop", "Shoe boutique"],
    keyStructures: ["Үүний том / жижиг хэмжээ байна уу?", "Өөр өнгө байгаа юу?", "Өмсөж үзэж болох уу?", "Энэ надад таарч байна"],
    expectedOutcome: "Learner negotiates size, fit, and color choices with a shop clerk."
  },
  {
    functionId: "comm_a1_23_bargaining_clarifying_price",
    title: "Bargain and Clarify Price at Open-Air Markets",
    mongolianTitle: "Зах дээр үнэ буулгах, наймаалцах",
    level: "A1",
    domain: "Transactional",
    prerequisites: ["comm_a1_20_asking_bill_payment"],
    communicativeGoal: "Politely negotiate discounts on multi-item purchases at open bazaars.",
    typicalScenarios: ["Naran Tuul market", "Souvenir vendor stalls", "Flea markets"],
    keyStructures: ["Үнээ жоохон буулгах уу?", "Хямдруулах боломж байна уу?", "Хоёрыг авбал хэд вэ?", "Сүүлийн үнэ хэд вэ?"],
    expectedOutcome: "Learner conducts respectful commercial negotiation using culturally normative phrasing."
  },
  {
    functionId: "comm_a1_24_asking_clock_time",
    title: "Ask For and Tell Current Clock Time",
    mongolianTitle: "Цаг асуух ба цаг заах",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_13_numbers_counting_1_to_100"],
    communicativeGoal: "Ask what time it is, tell the exact hour, half hours, and minutes past/to.",
    typicalScenarios: ["Checking train departure time", "Asking a passerby for the time", "Coordinating meetups"],
    keyStructures: ["Цаг хэд болж байна вэ?", "Яг гурван цаг болж байна", "Таван цаг хагас", "Зургаагаас арван минут өнгөрч байна"],
    expectedOutcome: "Learner states precise clock time using standard Mongolian temporal case constructions."
  },
  {
    functionId: "comm_a1_25_days_of_the_week",
    title: "State Days of the Week and Recurring Class Schedules",
    mongolianTitle: "Гариг өдрүүдийг нэрлэх, хичээлийн хуваарь ярих",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_24_asking_clock_time"],
    communicativeGoal: "Name weekdays and weekends, and state which days events take place.",
    typicalScenarios: ["Planning study days", "Confirming office operating hours", "Scheduling sports practice"],
    keyStructures: ["Өнөөдөр ямар гариг вэ?", "Өнөөдөр Даваа гариг", "Би Баасан гаригт завтай", "Хагас сайн өдөр уулзъя"],
    expectedOutcome: "Learner uses both formal planetary day names and colloquial numerical weekday names."
  },
  {
    functionId: "comm_a1_26_dates_months_calendar",
    title: "Express Calendar Dates, Months, and Birthdays",
    mongolianTitle: "Он сар өдөр, төрсөн өдрөө илэрхийлэх",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_25_days_of_the_week"],
    communicativeGoal: "State the date, name calendar months, and declare birth dates.",
    typicalScenarios: ["Filling out administrative forms", "Talking about holiday schedules", "Celebrating birthdays"],
    keyStructures: ["Өнөөдөр хэдэн бэ?", "Есдүгээр сарын хорин хоёр", "Таны төрсөн өдөр хэзээ вэ?", "Миний төрсөн өдөр таван сард"],
    expectedOutcome: "Learner states dates following Mongolian Year-Month-Day order with genitive suffixes."
  },
  {
    functionId: "comm_a1_27_daily_routines_morning_evening",
    title: "Describe Daily Routines and Personal Habits",
    mongolianTitle: "Өдрийн дэглэм, хийдэг зүйлсээ ярих",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_24_asking_clock_time"],
    communicativeGoal: "Recount morning wakeup, breakfast, work/study periods, and evening sleep schedules.",
    typicalScenarios: ["Language exchange diary sharing", "Explaining personal schedule to hosts"],
    keyStructures: ["Би өглөө долоон цагт босдог", "Өглөөний цайгаа уудаг", "Орой ном уншаад унтдаг"],
    expectedOutcome: "Learner uses the habitual aspect (-даг) and simple converbs to narrate a day."
  },
  {
    functionId: "comm_a1_28_asking_directions_street",
    title: "Ask For and Give Elementary Street Directions",
    mongolianTitle: "Зам асуух ба энгийн чиг заах",
    level: "A1",
    domain: "Transactional",
    prerequisites: ["comm_a1_12_location_simple_objects"],
    communicativeGoal: "Ask how to get to a landmark, and understand directions like straight, left, and right.",
    typicalScenarios: ["Finding a bank or pharmacy in town", "Asking pedestrian directions"],
    keyStructures: ["Төв шуудан хаана байдаг вэ?", "Шулуун яваарай", "Баруун тийшээ эргээрэй", "Зүүн талд нь байна"],
    expectedOutcome: "Learner follows directional prompts and orients movement along cardinal/relative axes."
  },
  {
    functionId: "comm_a1_29_taking_public_bus",
    title: "Inquire About Public Bus Routes and Bus Card Scanning",
    mongolianTitle: "Нийтийн тээврийн автобусны чиглэл лавлах",
    level: "A1",
    domain: "Transactional",
    prerequisites: ["comm_a1_28_asking_directions_street"],
    communicativeGoal: "Confirm which bus goes to a destination, locate bus stops, and manage bus fare cards.",
    typicalScenarios: ["Ulaanbaatar bus stop", "Asking passengers if bus stops at Peace Square"],
    keyStructures: ["Энэ автобус Их Дэлгүүр ордог уу?", "Дараагийн буудал юу вэ?", "U-Money картаа дарна уу"],
    expectedOutcome: "Learner navigates city bus transport by checking route numbers and stops."
  },
  {
    functionId: "comm_a1_30_hailing_street_taxi",
    title: "Hail an Unofficial Street Taxi and Agree on Destination",
    mongolianTitle: "Халтуур, такси барих, очих газраа хэлэх",
    level: "A1",
    domain: "Transactional",
    prerequisites: ["comm_a1_28_asking_directions_street", "comm_a1_20_asking_bill_payment"],
    communicativeGoal: "Signal a private car, state intended destination, and agree on per-kilometer or flat fare.",
    typicalScenarios: ["Hailing a ride on Peace Avenue", "Explaining drop-off spot to driver"],
    keyStructures: ["Хороолол орно, явах уу?", "Нэг километр нь хэд вэ?", "Гэрлэн дохион дээр бууна", "Энд зогсоорой"],
    expectedOutcome: "Learner successfully communicates destination and stopping point to taxi drivers."
  },
  {
    functionId: "comm_a1_31_weather_seasons_basic",
    title: "Comment on Daily Weather and Four Seasons",
    mongolianTitle: "Цаг агаар, жилийн дөрвөн улирлын тухай ярих",
    level: "A1",
    domain: "Informational",
    prerequisites: ["comm_a1_01_formulaic_greetings"],
    communicativeGoal: "Describe sunny, cold, windy, or snowy weather and express seasonal preferences.",
    typicalScenarios: ["Small talk while waiting for a friend", "Starting a phone call"],
    keyStructures: ["Өнөөдөр цаг агаар ямар байна?", "Өнөөдөр маш хүйтэн байна", "Цас орж байна", "Салхитай байна", "Хавар болж байна"],
    expectedOutcome: "Learner exchanges basic weather observations using standard adjectives and weather predicates."
  },
  {
    functionId: "comm_a1_32_likes_dislikes_simple",
    title: "Express Personal Likes, Dislikes, and Preferences",
    mongolianTitle: "Дуртай ба дургүй зүйлсээ илэрхийлэх",
    level: "A1",
    domain: "Interpersonal",
    prerequisites: ["comm_a1_06_self_introduction_name"],
    communicativeGoal: "State what food, music, or pastimes one likes or dislikes using дуртай/дургүй.",
    typicalScenarios: ["Chatting with friends over tea", "Choosing entertainment options"],
    keyStructures: ["Би монгол хоолонд дуртай", "Би цасанд дургүй", "Та юунд дуртай вэ?", "Би дуу сонсох дуртай"],
    expectedOutcome: "Learner attaches dative-locative to liked items and prospective participle (-х) to liked activities."
  },
  {
    functionId: "comm_a1_33_hobbies_free_time",
    title: "Discuss Hobbies, Sports, and Leisure Activities",
    mongolianTitle: "Чөлөөт цаг, хобби, сонирхлоо ярих",
    level: "A1",
    domain: "Interpersonal",
    prerequisites: ["comm_a1_32_likes_dislikes_simple"],
    communicativeGoal: "Describe free time activities such as reading, playing football, hiking, or movies.",
    typicalScenarios: ["Social clubs", "Getting to know classmates"],
    keyStructures: ["Чи чөлөөт цагаараа юу хийдэг вэ?", "Би ууланд алхдаг", "Би кино үздэг", "Би гитар тоглодог"],
    expectedOutcome: "Learner talks about regular recreational pursuits with habitual aspect."
  },
  {
    functionId: "comm_a1_34_classroom_instructions",
    title: "Follow Teacher Classroom Instructions and Commands",
    mongolianTitle: "Багшийн заавар, ангийн дүрэм сонсож ойлгох",
    level: "A1",
    domain: "Academic",
    prerequisites: ["comm_a1_01_formulaic_greetings"],
    communicativeGoal: "Respond to imperatives to open books, listen carefully, read aloud, and write down.",
    typicalScenarios: ["Language classroom instruction", "Listening to test guidelines"],
    keyStructures: ["Номоо нээнэ үү", "Анхааралтай сонсоорой", "Самбар луу хараарай", "Дэвтэртээ бичээрэй"],
    expectedOutcome: "Learner executes classroom tasks in response to polite imperative forms (-аарай)."
  },
  {
    functionId: "comm_a1_35_asking_language_clarification",
    title: "Ask for Repetition, Slower Speech, and Meaning",
    mongolianTitle: "Дахин хэлүүлэх, удаан яриулах, утга лавлах",
    level: "A1",
    domain: "Interpersonal",
    prerequisites: ["comm_a1_01_formulaic_greetings"],
    communicativeGoal: "Ask an interlocutor to repeat, speak more slowly, or explain what a word means.",
    typicalScenarios: ["When encountering rapid speech on the street or in stores", "During classroom exercises"],
    keyStructures: ["Дахиад нэг хэлнэ үү", "Жоохон удаан ярина уу", "Би ойлгохгүй байна", "Энэ ямар утгатай вэ?"],
    expectedOutcome: "Learner proactively repairs conversational breakdowns using standard meta-linguistic queries."
  }
];
