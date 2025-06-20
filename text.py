from dotenv import load_dotenv
import os

load_dotenv()  # підключення до закритого файлу
INST_URL = os.getenv('INST_URL')
# Практики

BOT_TEXT = {'bot_description': [('Чи бувало у вас таке, що знаходячись наодинці із самим собою, '
			'ви відчуваєте тяжкі емоції і не знаете, що з ними робити? 🤷🏻‍♂\n'
			'\n'
			'До того ж наші близькі та друзі не завжди можуть бути поруч, та підтримати нас, '
			'або дати дієву пораду і від цього стає ще більш сумно та самотньо...'),
			('Я був створений спеціально для цих випадків, коли тобі потрібна допомога '
			 'і ти не знаєш до кого звернутися, та як з цим впоратися.🤗\n'
			 '\n'
			'Я допоможу тобі краще зрозуміти себе і дам перевірені психологічні техніки для самопомочі, '
			'щоб тобі стало спокійніше і твоє життя стало трохи краще.🧑🏻‍🎓')]}

PRE_QUESTS = {'страх': [('Чи буває у вас таке, що іноді з першого погляду незначна подія, '
						'або маленька справа відверто викликають у нас відчуття некерованого страху? 🫣\n'
						'\n'
						'У такі моменти ми дізоріентовані і нам важко приймати усвідомлені рішення.\n'
						'Частіше за все, ми вимушені рухатися по внутрішній системі "бий, біжи, завмри".\n'
						'Все залежить тільки від випадку, або особистих налаштувань кожного. 👤\n'
						'\n'
						'Не маючи контроля над ситуацією, підкоряючись інтуїтивному відчуттю, '
						'ми стаємо заручниками обставин, про що потім часто жалкуємо. 😔\n'
						'\n'
						'Для того, щоб повернути собі контроль, ми постараємося зрозуміти свій страх, '
						'прислухатись та домовитись з ним. 🤝\n'
						'\n'
						'Адже насправді, наш страх є тим, хто турбується про нас, намагається захистити, '
						'а також те, що особисто для нас, є цінним.💎'),
						('Робота зі страхом буде поєднуватися з двох технік:\n'
						 '\n'
						 '1. "Техніка випередження страху" - це техніка, яка допоможе створити план, '
						 'якого ми будемо притримуватися у разі виникнення страху, або план його уникнення. 🔜\n'
						 '\n'
						'2. Декартові координати. 📏\n'
						'(але про неї тільки після виконання першої техніки)'
						 '\n'),
						('А тепер про "Декартові координати" - це техніка, яка допоможе глибше зрозуміти нам'
						 ' самих себе і те, що ми отримаємо, або втратимо'
						 ' зустрівшись зі своїм страхом один на один.📏')],
	'я не розумію що відчуваю': [('Якщо ви не розумієте, яку саме емоцію ви відчуваєте в моменті, '
						'з цього можна зробити декілька висновків:\n'
						'\n'
						'1. Ваші емоції, скоріш за все змішані і вам складно від\'єднати одну'
						' від іншої.\n'
						'Спробуйте роздивитись їх, як окремі частини цілого механізму і зосередитись '
						'на тому, з яких саме частин (емоцій) він зібраний. ☯\n'
						'\n'
						'2. Вам взагалі складно зрозуміти і визначити свої емоції, '
						'адже ви рідко дослухаєтесь до них і загалом керуєтесь логікою та фактами. 📊\n'
						'В будь якому разі не переймайтесь, адже це навичка і вона'
						' чудово тренується з часом. 💪\n'
						'\n'
						'Саме з цим ми і будемо тут працювати користуючись відомими техніками, '
						'але досі дієвими.\n'
						'\n'
						'P.S\n'
						'Для кращого розуміння, які взагалі бувають емоції та як змішуються, '
						'ми додали фото на початку.\n'
						'Чи є там щось схоже на ваші?'),
						('Для того, щоб визначити свої емоції їх треба помітити, зафіксувати та відчути. 🧘‍♀\n'
						'\n'
						'Саме з цим нам і допоможуть ці дві техніки пов\'язані між собою, '
						'тому використовувати їх потрібно <b> виключно по черзі </b>. 🧩'),
						 ('Тепер, коли ми навчилися записувати, а отже відстежувати свої емоції, '
						'давайте дізнаємось чому ті, чи інші емоції з`являються у вас та з '
						'якими реальними ситуаціями вони пов\'язані. ⚛')],
			'злість': [('Головне на що варто звернути увагу, так це те, '
						'що злість - це емоція, яка є провідником у наше краще, '
						'через відсторонення від гіршого для нас. ⛔\n'
						'\n'
						'Вона про порушення тих речей, що важливі для нас, а саме:\n'
						'▫ "зі мною так не можна"\n' 
						'▫ "коло спілкування в якому мені не комфортно"\n'
						'▫ "не справедливість по відношенню до мене"\n'
						'▫ "мої переконання, бажання, відчуття не беруть до уваги"\n'
						'\n'
						'Тому що люди, або порушують мої цінності та переконання, '
						'або ж поводять себе таким чином, яким би я не вчинив з ними.\n'
						'\n'
						'Але на жаль некерована та пригнічувана злість, руйнує нас самих і те, що є для нас цінним. 😥\n'
						'\n'
						'Тому так важливо розібратися у чому першопричина і навчитися керувати нею. '
						'Керувати, розуміти та проявляти, а не контролювати і пригнічувати.\n'
						'\n'
						'Інакше злість повернеться до нас вже в інших формах. 😈'),
						('Перше, що потрібно зробити коли ми відчуваємо злість, це висловити нашу емоцію доступним '
						'та безпечним для оточуючих способом, прийшовши до відчуття рівноваги та спокою. ⚖\n'
						'\n'
						'Далі ж потрібно зрозуміти, що саме її викликає. 🤔\n'
						'\n'
						'Почнемо з першого:'),
						('Тепер, коли ми навчилися безпечно проявляти емоцію, '
						'та не блокувати її, а головне, покращили свій загальний стан, '
						'слід поміркувати про її першопричини. 🤔\n'
						'\n'
						'Давайте поміркуємо над тим, чому саме вона виникає, '
						'які саме кордони були порушені, та як зробити так, щоб не зустрічатися з нею занадто часто. 🧘‍♀')],
			'тривога': [('Чи буває у вас таке, що іноді зовнішні обставини життя '
						'лякають вас і від цього з\'являється тривога? '
						'Страх сковує вас і вам тяжко зосередитися на будь-чому, '
						'або ж просто робити повсякденні речі у своєму житті. ⛓\n'
						'\n'
						'Ви відчуваєте себе беззахисно та у небезпеці і не знаєте що з цим робити. ' 
						'Особливо коли тривога не має чітко визначеної причини. 🤷‍♂\n'
						'\n'
						'У таких випадках, найперше  що треба зрозуміти, це те, '
						'що це абсолютно нормальна адаптивна реакція нашого організму на зовнішні тригери, '
						'яка існує в нашому організмі, як корисна програма, що стимулює '
						'та підсвічує актуальні для нас питання і дає емоційний стимул для їх вирішення. 🦾\n'
						'\n'
						'Але іноді тривога буває безпричинна, а це означає, що вона має підсвідомий характер.'
						'Та головне питання тут, як перемогти те, що навіть не взмозі побачити? 👁️\n'
						'Але про це іншим разом.\n'
						'\n'
						'Наразі, в цьому блоці, ми розглянемо тільки техніки поліпшення власного стану, '
						'та зниження рівня тривоги.\n'
						'Для більшого я ж рекомендую працювати вам зі спеціалістом. 💙'),
						('Найперше, що потрібно зробити для того, щоб вийти з цього замкненого кола'
						' і не потонути в болоті тривожних думок, щодо власного стану, '
						'це змістити фокус уваги з внутрішнього стану на зовнішній світ. 🌇\n'
						'\n'
						'З цим нам допоможе перша, доволі проста техніка.'),
						('Тепер коли ми знаємо, як базово знизити рівень тривоги, '
						'я пропоную створити дещо особливе із власних спогадів. 🥰\n'
						'\n'
						'Місце у якому завжди затишно та спокійно, місце до якого '
						'ми завжди можемо повернутися і насолодитися цим приємним моментом. 💙')],
			'провина': [('Чи є правдою те що я зараз розкажу про вас?\n'
						'\n'
						'Дуже часто ви відчуваєте, що ваша поведінка не є вірною, '
						'ви занурюетесь у роздуми про те як потрібно було себе повести або що сказати, '
						'та у більшості випадків не відповідаєте бажанням та потребам інших, '
						'регулярно жалкуєте та звинувачаєте себе за свої вчинки минулого.'
						'Часто вибачаючись та відчуваючи себе нікчемною людиною. 😔\n'
						'\n'
						'Все це про провину, тому перше та найголовніше, що потрібно сказати щодо цього це те, '
						'що вона виникає на фоні внутрішнього суб\'єктивного відношення щодо своїх вчинків, '
						'дій та їх наслідків. 💭\n'
						'\n'
						'У провини є дві сторони: світла та темна.\n'
						'\n'
						'Перша допомагає нам бути емпатичними та чуттєвими до інших їх бажань та потреб, '
						'змінюючи власну поведінку за рахунок власних висновків сформованих за рахунок провини.'
						'І ви навряд чи були б тут якби вас хвилювала перша. 🤍\n'
						'\n'
						'Друга ж, темна та токсична, змушує нас відчувати себе винними за ті речі та людей '
						'які є поза межами нашого власного контролю, такі як минуле або поведінка інших.'
						'Вона руйнує нас самих зсередини, та значно ускладнює життя 🖤\n'
						'\n'
						'Тому, наразі ми роздивимось другий випадок "темну сторону", '
						'та спробуємо зрозуміти як позбутися від токсичного відчуття провини. 🚮'),
						('Найперше на що слід звернути увагу, так це те, '
						'що відчуття провини повністю захоплює нас у полон. 🔒\n'
						'\n'
						'І чим довше ми занурюємося  у наші роздуми, тим більше відчуваємо провину, '
						'закінчуючи на тому, що ми загалом "погана" особистість, '
						'а не просто припустилися помилки у житті . ⚠\n'
						'\n'
						'Тому наразі будемо відокремлювати шипи від троянд, а саме себе від відчуття провини. 🌹'),
						('Тепер, коли ми об\'єктивно подивилися на власне відчуття провини, '
						'знизивши його рівень, давайте перетворимо його в "дещо на що ми можемо вплинути". 🤝\n'
						'\n'
						'А саме на те, що я можу з цим зробити, '
						'або як вплинути на ситуацію зараз, щоб не відчувати більше провини щодо цього. 🚮')],
			'сум': [('Іноді по не зрозумілим нам причинам ми відчуваємо сум, '
					'у ці моменти частіше за все нам хочется побути наодинці, '
					'втікти від світу, та інколи просто заховатися під ковдру, '
					'ні про що не думати, відпочити та просто поспати. 🛌\n'
					'\n'
					'До того ж, ви напевно помічали, що іноді сум є точкою входу для більш тяжких емоцій, '
					'занурюючись у неї дуже глибоко ми можемо відчути - провину, сором, стурбованість, '
					'самотність, безвихідність та тотальний відчай.\n'
					'\n'
					'Сум це емоція, яка виникає частіше за все внаслідок значної незадоволеності деяких '
					'аспектів нашого життя, інтуїтивно зрозумілих або навіть неусвідомлених. 🤔\n'
					'\n'
					'До того ж, в невеликих дозах, вона є корисною, адже саме таким чином ми відпочиваємо, '
					'та маємо змогу структурувати думки та повністю прожити важливі ситуації минулого. 🧘\n'
					'\n'
					'Тому, наразі ми будемо шукати особисті шляхи нормалізації стану, '
					'та спробуємо зрозуміти щодо чого ми сумуємо. 🕵️'),
					('Для того, щоб стабілізувати власний стан, '
					'давайте звернемо нашу увагу на те, що зворотній бік суму - це радість. 🎭\n'
					'\n'
					'Тому, наразі ми будемо шукати або згадувати все те, що робить нас щасливими, '
					'приносить радість, та змушує відчути себе живою людиною. 💃'),
					('Тепер коли ми знайшли власні дієві засоби поліпшення стану, '
					'давайте зосередимося на тому, про що саме хоче сказати нам ця емоція. ❓\n'
					'\n'
					'Адже сум - це, частіше за все, про минуле і те в ньому, що для нас є цінним. 💎')]}

ALL_QUESTS = {'страх': [(''), ('Для цієї вправи нам знадобиться:\n'
						'\n'
						'-аркуш паперу або нотатки смартфона\n'
						'-ручка або олівець\n'
						'\n' 
						'Поділіть аркуш паперу на три умовні колонки:\n'
						'\n'
						'▫ Першу ми назвемо\n' 
						'"мій страх" - сюди запишемо те чого ми боїмося.\n'
						'\n' 
						'▫ Друга колонка називаеться "попереджуюча подія" сюди ми зазначимо те що '
						'можемо зробити для того, щоб не зустрітися зі своїм страхом.\n'
						'\n'
						'▫ Третя колонка називаеться "мій план якщо.. " - запишемо те що ми можемо зробити,'
						' або зробимо якщо наш страх стане реальністю і ця подія вже відбудеться.'),
						('Для цієї техніки нам знадобиться:\n'
						'\n'
						'-аркуш паперу\ручка або олівець\n'
						'-нотатки смартфона\n'
						'\n'
						'Розкресліть, як зазначено на малюнку, аркуш на чотири частини і напишіть в них наступне:\n'
						'\n'
						'▫ Що я отримаю, якщо я не зроблю те чого боюсь?\n'
						'▫ Що я отримаю, якщо я зроблю те чого боюсь?\n' 
						'▫ Що я втрачу, якщо не зроблю те чого боюсь?\n'
						'▫ Що я втрачу, якщо зроблю те чого боюсь?\n'
						'\n'
						'Памятайте, що кожне наше, навіть негативне рішення, '
						'завжди має якісь позитивні наслідки для нас.\n'
						'\n'
						'Наше завдання їх побачити і зрозуміти!')],  # кортежи
	'я не розумію що відчуваю': [(''), ('Щоденник емоцій:\n'
						'\n'
						'▫ Відкрийте на своєму смартфоні додаток "нотатки" і протягом дня, '
						'хоча б тричі записуйте те, що відчуваєте в цей момент.\n'
						'▫ Для того щоб не забути записати їх протягом дня, встановіть на своєму смартфоні '
						'"будильники" з часовим проміжком в три години, підписавши його "щоденник емоцій".\n'
						'▫ У момент коли спрацьовує "будильник", відкривайте "нотатки" і запитуйте у себе: "що '
						'я зараз відчуваю?" записуючи отриманний результат.\n'
						'▫ Протягом 7-14 днів записуйте свої емоції у нотатки, щоб виробити нову корисну звичку '
						'і зрозуміти себе.'),
						 ('Самоспостереження:\n'
						'\n'
						'У момент запису емоції у щоденник, дайте собі відповідь на наступні питання, '
						'записуючи отриманний результат поряд з вашою емоцією.\n'
						'\n'
						'▫ Що викликало у меня цю емоцію?\n'
						'▫ Що я робив/ла коли виникла ця емоція.\n'
						'▫ Що я думаю з приводу своєї емоції\n'
						'▫ Що я відчув/ла фізично у момент емоції\n'
						'\n'
						'P.S. Чи є причинно-наслідкові зв\'язки між ситуацією та вашою емоцією, '
						'та як ви дієте або що думаєте у момент їх відчуття.')],
			'злість': [(''), ('Лист злості:\n'
						'\n'
						'Для цієї вправи нам знадобиться:\n'
						'\n'
						'- Аркуш паперу\ручка або олівець\n'
						'- Нотатки смартфона\n' 
						'\n'
						'Візьміть аркуш паперу і напишіть на ньому все, '
						'що вас дратує, бісить і злить зараз:\n'
						'\n'
						'▫ Люди.\n'
						'▫ Думки.\n'
						'▫ Обставини.\n'
						'▫ Ситуації.\n'
						'▫ Відчуття.\n'
						'▫ Емоції.\n'
						'▫ Слова або дії інших або власні.\n'
						'\n'
						'Обовя\'зково ретельно все перевірте і переконайтесь, що нічого не забули записати, '
						'навіть найпотаємнішого, або того, що забороняєте собі відчувати.\n'
						'\n'
						'Після чого подивіться ще раз на аркуш, що злить вас і знищіть його будь яким способом, спаліть'
						', розірвіть, пошматуйте або ж просто викиньте у смітник разом із аркушем все те, '
						'що турбує вас зараз.'),
						('Самоаналіз:\n'
						'\n'
						'▫ Поміркуйте над тим, яке ваше бажання було порушено, чого ви бажали насправді, '
						'або чого потребували у момент виникнення злості?\n'
						'\n'
						'▫ Визначте хто, або що викликало у вас злість, '
						'чи є можливим повернути цю емоцію адресату екологічно?\n'
						'\n'
						'▫ Поміркуйте про те, якими саме способами, без шкоди для себе та інших, '
						'ви можете проявляти свою злість у майбутньому, стикаючись з нею.\n'
						'\n'
						'▫ Якщо ви розумієте, що проявити, або повернути свою злість не є можливим, '
						'дозвольте собі сумувати\горювати, таким чином проживаючи свою емоцію, '
						'але ні в якому разі не забороняючи відчувати собі власні складні почуття.')],
			'тривога': [(''), ('Фокус уваги:\n'
						'\n'
						'Коли ви відчуваєте наближення тривоги, або ж вже знаходитесь у її полоні, '
						'спробуйте сфокусуватися на зовнішньому нейтральному объекті у вашому полі зору, '
						'при можливості доторкнувшись до нього, фокусуючись на ньому '
						'та роздивляючись його до дрібниць, наче ви дослідник:\n'
						'\n'
						'▫Яку він має форму?\n▫Якого він кольору?\n▫Який завбільшки?\n'
						'▫Яка текстура предмету?\n▫Який на дотик?\n І т.п.\n'
						'\n'
						'У цей момент, повільно порахуйте про себе до 20-ти, фокусуючись тільки на об\'єкті.\n'
						'При необхідності повторіть вправу збільшуючи число до тих пір, поки '
						'ви не відчуєте покращення свого стану.\n'
						'\n'
						'Будьте терплячі, іноді це може зайняти трошки більше часу, '
						'аби повністю зануритися у стан спокою.\n'
						'Терплячість та зосередженість ваші головні помічники 💙'),
						('Щасливий спогад:\n'
						'\n'
						'Спробуйте згадати момент зі свого минулого, в якому ви відчували щастя.\n'
						'Момент, який на усе життя закарбувався у ваших відчуттях, '
						'як щось неймовірно тепле, приємне та світле.\n'
						'\n'
						'Момент, який змусив закохатися вас у це життя і його різнобарвність.' 
						'Де ви відчували себе безпечно, комфортно, розслаблення, спокійно та легко.\n'
						'\n'
						'Занурюючись у нього згадайте :\n'
						'\n'
						'▫Яка це була пора року?\n' 
						'▫Скільки вам було років?\n'
						'▫У що ви були одягнені та як вигладали?\n'
						'▫Чи був хтось поруч з вами?\n' 
						'▫Чим ви займалися у цей момент?\n'
						'▫Про що ви думали?\n' 
						'▫Що було навколо вас?\n'
						'\n'
						'P. S.\n' 
						'Для більшого занурення у приємні спогади, ми додали для вас аудіофайл, '
						'який допоможе налаштуватися на потрібний лад, використайте його. 😉')],
			'провина': [(''), ('Сеперація провини:\n\nДля цієї вправи нам знадобиться:\n'
						'- Аркуш паперу\ручка або олівець\n'
						'- Нотатки смартфона'
						'\n'
						'Розкресліть аркуш паперу на 4 колонки, як вказано на малюнку, '
						'прописавши у кожній наступні запитання:\n'
						'\n'
						'▫За що саме я відчуваю провину?\n'
						'▫Чи були додаткові обставини в цій ситуації, що не залежили від мене?\n'
						'Наприклад - інші люди, їх дії випадковості, тощо.\n' 
						'▫Чи реально я можу контролювати, керувати та відповідати за усі дії та відчуття інших людей?\n'
						'▫Які у мене, як у особистості є позитивні або "сильні" сторони?\n'
						'\n'
						'Виконуючи вправу зосередтесь на одній окремій, хвилюючій саме зараз, вас ситуації, '
						'точно розібравшись у чому саме є ваша провина, '
						'а що є її темною,токсичною, необ\'єктивною стороною.\n'
						'\n'
						'P. S.\n' 
						'Намагайтеся бути об\'єктивними і чесними із собою, наскільки це можливо.'),
						('Градація провини:\n'
						'\n'
						'▫Згадайте усе, що нещодавно викликало у вас відчуття провини, '
						'тезисно прописавши ці 5-10 речей за які ви себе звинувачували.\n'
						'\n'
						'▫Оберіть ту ситуацію, яку на вашу думку, найлегше всього виправити.\n'
						'\n'
						'▫Спираючись на свої сильні сторони, які ви прописали у "техніці 1", '
						'подумайте та запишіть, що саме ви можете зробити для того, щоб вирішити цю ситуацію.\n'
						'\n'
						'P. S.\n'
						'Навіть якщо це не допоможе виправити ситуацію, '
						'ви зможете сказати собі - "я зробив все, що залежило від мене", '
						'а отже досягнете головної нашої мети - позбудетесь відчуття провини.')],
			'сум': [(''), ('Пошук свого ресурсу.\n'
						'\n'
						'Для виконання цієї вправи нам знадобиться:\n'
						'- Аркуш паперу\ручка або олівець\n'
						'- Нотатки смартфона\n'
						'\n'
						'Виконуючи наступну вправу, зверніть увагу на те, '
						'що ви можете знайти відповіді не на усі питання і це нормально, '
						'адже наше головне завдання зрозуміти та помітити для себе, '
						'які у нас є сильні сторони, та як вони допомагають нам відчувати себе краще.\n'
						'\n'
						'Дайте відповідь на наступні питання :\n'
						'▫Що для вас завжди є цінним, та у що ви вірили у найтемніші часи вашого життя?\n'
						'\n'
						'▫Які ваші хоббі та захоплення завжди підіймають вам настрій?\n'
						'\n'
						'▫Коли ви засмучені, з ким ви в першу чергу хочете цим поділитися та чию отримати підтримку?\n'
						'\n'
						'▫Про що ви мрієте у майбутньому, та які теплі спогади завжди покращують вам настрій?\n'
						'\n'
						'▫Нові знання, а саме процесс навчання та освоєння нових навичок робить ваше життя більш цікавим?\n'
						'\n'
						'▫Що матеріальне та фізичне допомагає вам відчути себе краще?\n' 
						'Спорт, їжа, прогулянки, музика, тощо.\n'
						'\n'
						'Чесно відповівши на ці запитання, '
						'ви отримаєте індивідуальний комплекс речей '
						'що, робить саме ваше життя краще, використовуйте його.\n'
						'\n'
						'P. S.\n' 
						'Головне пам\'ятайте про те, що у всьому має бути міра та баланс.\n'
						'Адже шматочок торту дійсно може принести радість, а от цілий торт навряд чи.'),
						('Саморефлексія:\n'
						'\n'
						'Для виконання вправи нам знадобиться:\n'
						'- Аркуш паперу\ручка або олівець\n' 
						'- Нотатки смартфона\n'
						'\n'
						'Як ми вже з\'ясували, сум - це эмоція про минуле, '
						'тому давайте розглянемо на одному окремому випадку з вашого минулого, '
						'про що саме та за чим ви сумуєте.\n'
						'\n'
						'▫Для цього згадайте ситуацію, яка викликає це почуття і спробуйте подивитися на те, '
						'що важливого було  для мене в ній на рівні особистих цінностей. ' 
						'Наприклад: відносини, коло друзів, інтереси, можливості, відчуття свободи, тощо.\n'
						'\n'
						'▫Чи відображають ці речі мене як особистість, та чи відчуваю я потребу у них саме зараз?\n'
						'\n'
						'▫На які важливі, особисто для мене, речі сум хоче звернути мою увагу?\n'
						'\n'
						'P. S.\n' 
						'Відповівши на питання, запишіть отриманий результат, '
						'та уявіть як саме вони покращать ваше життя, '
						'та що саме ви відчуєте коли отримаєте їх?')]}

RETARGET_QUESTIONS = {'страх': [('Частіше за все вас лякає те що буде, або ж те що вже колись було?'),
								('Подумайте про те що лякає вас найбільше, як гадаєте чому саме це?'),
								('Чи стає вам страшно у нових компаніях, містах, тощо?'),
								('Чи відчуваєте ви страх коли пробуєте щось нове?'),
								('Чи страшно вам залишатися наодинці із собою і чому якщо так?'),
								('Вам страшно розповідати щось про себе людям, чому?'),
								('Чи страшно для вас поділитися чимось особистим зі своїми рідними/ партнером?'),
								('Чи демонструєте/розповідаете6 ви іншим про свої темні сторони, та не найкращі прояви?'),
								('Наскільки складно для вас бути повністю відвертими з навколишнім світом і чи хотілось би вам бути відвертими на 100%?'),
								('Що ви робите коли вам стає дуже страшно і чи допомога це вам?')],  # кортежи
	'я не розумію що відчуваю': [('Наскільки складно вам приймати одноосібно важливі рішення в своєму житті?\n'
								'Згадайте з ким ви зазвичай радитесь.'),
								('Чи часто відбувається так, що ваш вибір напряму залежить від думки більшості?'),
								('При прийнятті рішення ви перш за все слухаете себе чи близьких, чому?'),
								('У вашому дитинстві ваші батьки часто вирішували за вас, що вам робити або як проводити час?'),
								('Наскільки складно для вас придбати собі одежу не прислухаючись до думки інших, або навіть не дивлячись на неї?'),
								('Ви відчуваєте себе так, ніби ви досі дитина і батьки продовжують контролювати ваше життя?'),
								('Коли ви відмовляете іншим людям якої ви про себе думки?'),
								('Чи складно вам відмовити іншим людям і які почуття це викликає у вас?'),
								('Те життя яке ви проживаете зараз влаштовує більше вас, чи ваших рідних?'),
								('Чи схожий ваш партнер на когось з ваших рідних, у чому ця схожість та як це впливає на ваше життя?'),
								('Чи складно для вас закінчувати ті справи, що ви почали з великим ентузіазмом?'),
								('Хто, на вашу думку, більше за все вплинув на вас у питанні вашої індивидуальності?'),
								('До кого, на вашу думку, краще прислухатися у вирішенні власних питань - друзів чи незнайомих людей, чому?'),
								('Чи є світ, та люди у ньому зрозумілими для вас, чому?'),
								('Гірка правда, чи брехня заради вищої позитивної мети, чому?'),
								('Що для вас важливо в інших людях, які саме риси характеру, здібності чому?'),
								('Якою людиною ви хотіли б бути, та якою є насправді?'),
								('Мета виправдовує засоби? Чому саме ви так вважаєте, та чи бувають винятки з правил?'),
								('Як вам наш бот, чи порадили б ви його друзям?'),
								('Напишіть 5 ваших сильних сторін як особистості і 5 слабких. Що ви відчуваєте з приводу цього?')],
					'тривога': [('Чи зіштовхувалися вы колись з панічними атаками, чи є це проблемою, та як часто вони бувають у вас?'),
								('Що саме ви робите коли вам тривожно та чи надовго вам це допомагає не відчувати тривогу?'),
								('Чи користувалися ви аффірмаціями/медитаціями, для покращення свого стану, чи робочий це інструмент для вас?'),
								('Чи схильні ви "колупати себе" коли ви нервуэте та відчуваєте тривогу?'),
								('Як часто ви думаєте про те, що з вами щось не так, на відміну від інших і саме тому ви нещасливі?'),
								('Коли вы згадуєте про "щасливі часи" що саме спадає вам на думку, як ви відчували себе в той момент і як зараз?'),
								('Чи часто ви думаєте про те, що чогось не встигнете і потрібно поспішати жити? Адже всі ми колись помремо.'),
								('Постійні вигорання, втома та апатія знайомі вам, та що ви робите зазвичай в таких випадках?'),
								('У вашому побуті ви притримуєтесь перфікціонізму та ідеальної чистоти?\nЧи критикували вас за це?'),
								('Чи використовуєте ви алкоголь, як спосіб зниження тривоги, та покращення загального стану?')],
						'провина': [('Чи часто ви звинувачаэте себе за "помилки минулого" які змінити вже не можна?'),
								('Чи часто ви відчуваєте провину перед своїми близькими та рідними вам людьми?'),
								('В ситуації конфлікту, ви частіше звинувачуєте себе, чи інших?'),
								('Ви звинувачуєте себе за те яка ви людина, і те чим займаєтесь?'),
								('Якими саме діями ви "караєте себе", коли відчуваєте провину?'),
								('Чи звинувачуєте ви себе за те, що маєте більше ніж інші, або живете краще інших?'),
								('Як часто ви чули у дитинстві від батьків "тобі має бути соромно за..."?'),
								('Коли в вашому житті щось йде не за планом ви звинувачуєте себе, або інших, чому так?'),
								('Ви краще відчуваєте себе коли ви, винуваті чи невинні в очах більшості?'),
								('Чи відчуваєте ви себе слабкими, поганими та безпорадними, відчуваючи провину?')],
					'злість': [('Чи часто ви відчуваєте злість і з якого приводу частіше за все?'),
								('Частіше за все, ваша злість спрямована на себе чи на інших?'),
								('Чи вважаєте ви що сердитися, злитися, гніватисяне можно і треба вміти контролювати свої емоції не проявляючи негативні і чому?'),
								('Що в інших людях викликає в вас некеровану злість, яка поведінка або риси характеру?'),
								('Що саме, в вас самих, злить вас найбільше?'),
								('Злитися це погано, або добре та чому саме ви так вважаєте?'),
								('Що у ваших рідних, друзях та близьких, злить вас найбільше?'),
								('Чи багато злості та злого у вашому житті і з чим це пов\'язано?'),
								('Якби вам було дозволено будь що коли ви у стані злості щоб ви робили, як саме проявляли себе?'),
								('Як саме, ви частіше за все виплескуєте свою злість і чи надовго це вам допомагає?')],
						'сум': [('За чим в минулому ви сумуєте більше за все?'),
								('Чи часто вам буває сумно і про що саме ви думаєте в такі моменти?'),
								('Коли ви дивитесь на своє життя зі сторони, чи стає вам сумно і що саме ви б хотіли в ньому змінити або повернути?'),
								('Чи часто ви повертаєтесь у свої спогади посумувати і чи є в них щось гарне окрім смутку;\n'
								'За чим саме ви повертаєтесь насправді?'),
								('Чи є у вас порядок дій щоб вийти із відчуття смутку, який і чи дійсно це допомогає вам?'),
								('Що позитивного є для вас у смутку і чи буває це інколи корисно?'),
								('Чи подобається вам інколи сумувати, або ж ви вважаєте що цього ніколи не непотрібно робити, чому? '),
								('В яких випадках, та поряд з якими людьми, вам частіше за все буває сумно?'),
								('Що у житті вас засмучує більше за все?'),
								('За чим саме в вашому житті ви сумуєте найбільше? (люди, події, моменти)')]
}
# в усіх фото треба було змінити лінк, додати:(uc?id='id-photo')
MEDIA = {'страх': [('https://drive.google.com/uc?id=1lrQUwrIcR09HB8jgEU1LNy8RArQ5Z9KG'),
					('https://drive.google.com/uc?id=1YTWZqZE4qpwaHIx0MxEm90l62v1QY0Np')],
		'я не розумію що відчуваю': [('https://drive.google.com/uc?id=1EMwAoF298wSY7eqwYRaISrsJziGCjcjj'),
					('https://drive.google.com/uc?id=1ETDzEcCAau4mFXIZ52-MYaCcFWB6kEeJ'),
					('https://drive.google.com/uc?id=1GDMD1G8an4Vwe8nkAhzoHDY-h3zpX-eW')],  # єдине фото в передописі
		'тривога': [('https://drive.google.com/uc?id=1Fb-KOTu0NAzcM1JgaUc1s_90QalVk6tx'),
					('https://drive.google.com/uc?id=1EbzmY0oVUtAfd3ixklmhMWA80ErJmawy'),
					('https://drive.google.com/uc?id=1D-3CVx736m0Fzn49itmqREgeRhR3GRu1')],  # музика
		'провина': [('https://drive.google.com/uc?id=1SuaCGCt21IgtbRR-GSJOOkS2bSZl8RYH'),
					('https://drive.google.com/uc?id=1H8b0JKywwHvUNXsFPrwNpSzubztLTw56')],
		'злість': [('https://drive.google.com/uc?id=1F20qR7fYOdlRHMBffVCeYHKnJrWmwWN0'),
				('https://drive.google.com/uc?id=1EzOP4CuJS9h1JblsD6G8ZUDchjO_eTUv')],
		'сум': [('https://drive.google.com/uc?id=1Ef1qL1LXRQTpeVjYemwa6zbevp_G6rAZ'),
				('https://drive.google.com/uc?id=1EwpYPOWpLAMawsbxZF1D3dDqxQYzSWa-')]
}

CALL_BACK_TEXT = [('Ми дуже цінуємо користь отриману вами від продукту, тому оцініть наскільки саме, '
				'у грошовому еквіваленті, він був корисним та допоміг у вирішенні проблеми, '
				'або ж покращив загальний стан. 💙\n'
				'\n'
				'Додатково зазначу що, за кожний донат 💳 понад 250 грн ви можете отримати:\n'
				'\n'
				'▫практичні рекомендації.\n▫додаткові техніки.\n▫технології подолання тяжких емоцій.\n▫та багато іншого...\n\n' 
				'Від практикуючого психолога, '
				'для вирішення особисто вашого питання враховуючи індивідуально вашу ситуацію.\n'
				'\n'
				'P. S.\n'
				'Для цього після оплати зробіть скріншот переказу та надішліть його, '
				f'разом з вашим питанням на сторінку <a href="{INST_URL}">Instagram</a>. 📲\n\n'
				'Номер карти для підтримки проекту:\n\n'
				'<code>5375 4115 0935 8326</code>'),
				('Якщо ви відчуваєте, що техніки не допомогають, зверніться до спеціаліста, '
				'щоб ми могли допомогти вам отримати бажаний результат якомога швидше.'),
				('Сподіваюсь ми допомогли вам покращити ваш стан. 🧘‍♀\n\n'
				'Якщо ви відчуваєте що це було цінним для вас, підтримайте наш проєкт. 💙'),
				('Наразі, я не можу зрозуміти чому ваш стан не змінився 🤷‍♂\n\n'
				'Спробуйте обрати іншу техніку чи поставити питання спеціалісту, щоб покращити ваш стан 💙'),
				('Для того, щоб точно визначити ваш стан, спробуйте ще раз пройти техніки.'),
				('Якщо ваш стан не змінився або погіршився, скоріш за все у вас дуже комплексна '
				'та індивідуальна ситуація в якій існує багато другорядних чинників  впливу, '
				'які не може відчути бот - але може зрозуміти людина.\n'
				'\n'
				'Або ж використати нашу спеціальну функцію "донат", '
				'в якій за кожний донат 💳 понад 250 грн ви отримаєте:\n'
				'\n'
				'▫практичні рекомендації щодо вирішення.\n▫додаткові техніки покращення стану.\n'
				'▫технології подолання тяжких емоцій.\n▫діагностичний аналіз ситуації\n\n' 
				'Від практикуючого психолога, для вирішення особисто вашого питання враховуючи '
				'усі фактори впливу та ситуацію.\n'
				'\n'
				'P. S.\n'
				'Для цього після оплати зробіть скріншот переказу та надішліть його, '
				f'разом з вашим питанням на сторінку <a href="{INST_URL}">Instagram</a>. 📲\n\n'
				'Номер карти для підтримки проекту:\n\n'
				'<code>5375 4115 0935 8326</code>')]