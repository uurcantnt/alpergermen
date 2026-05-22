/* ───────────── mobile menu ───────────── */
(function(){
  const burger=document.getElementById('burger'),mmenu=document.getElementById('mmenu');
  if(!burger||!mmenu)return;
  function toggle(o){burger.classList.toggle('x',o);mmenu.classList.toggle('open',o);document.body.style.overflow=o?'hidden':'';}
  burger.addEventListener('click',()=>toggle(!mmenu.classList.contains('open')));
  const close=document.getElementById('mclose');
  if(close)close.addEventListener('click',()=>toggle(false));
  mmenu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>toggle(false)));
})();

/* ───────────── practice areas ───────────── */
const AREAS=[
  {name:'Ceza Hukuku',desc:'Soruşturma ve kovuşturma aşamalarında şüpheli ve sanığın haklarının korunması; ifadeden temyize savunma.',tags:['Ağır ceza & asliye ceza','Tutuklamaya itiraz','Bilişim suçları','Trafik kazası ceza süreçleri'],
   nedir:'Ceza Hukuku Avukatı Nedir?',
   ned:'Ceza hukuku avukatı, suç isnadıyla karşılaşan bireylerin soruşturma ve kovuşturma aşamalarında hukuki haklarını koruyan avukattır. Şüpheli veya sanığın ifade vermesinden tutukluluğa itiraz, duruşma sürecinden temyiz aşamasına kadar tüm ceza yargılaması boyunca savunma hizmeti sunar.',
   steps:[['İfade ve sorgu aşamasında temsil','Kolluk ve savcılık aşamasında müvekkilin haklarını koruyarak ifade sürecinin yönetilmesi.'],['Tutukluluk ve adli kontrol kararlarına itiraz','Haksız tutuklama veya adli kontrol kararlarına karşı itiraz dilekçelerinin hazırlanması.'],['Duruşma savunmasının hazırlanması','Delillerin değerlendirilmesi, tanık dinlenmesi ve mahkeme savunmasının stratejik olarak yürütülmesi.'],['Temyiz ve kanun yolu başvuruları','İlk derece mahkemesi kararlarına karşı istinaf ve Yargıtay başvurularının hazırlanması.']]},
  {name:'Aile Hukuku',desc:'Evlilik, boşanma, velayet, nafaka ve mal paylaşımı gibi aile ilişkilerinden doğan uyuşmazlıklarda taraflara hukuki destek.',tags:['Çekişmeli & anlaşmalı boşanma','Nafaka ve velayet','Mal paylaşımı','Tanıma ve tenfiz'],
   nedir:'Aile Hukuku Avukatı Nedir?',
   ned:'Aile hukuku avukatı; evlilik, boşanma, velayet, nafaka ve mal paylaşımı gibi aile ilişkilerinden doğan uyuşmazlıklarda taraflara hukuki destek sağlayan avukattır. Aile davaları yalnızca evlilik birliğinin sona erdirilmesiyle sınırlı değildir; çocuk velayeti, nafaka, mal rejimi tasfiyesi ve tazminat gibi birçok konuyu da kapsar.',
   steps:[['Boşanma dilekçesinin hazırlanması','Davanın hukuki stratejisine uygun, eksiksiz dilekçe hazırlığı ve mahkemeye sunumu.'],['Delillerin toplanması ve sunulması','Davanın seyrini belirleyecek delillerin profesyonel olarak derlenmesi ve mahkemede sunulması.'],['Nafaka ve tazminat taleplerinin hazırlanması','Müvekkilin haklarına uygun nafaka ve tazminat taleplerinin belirlenmesi ve takibi.'],['Velayet ve kişisel ilişki düzenlemeleri','Çocuğun üstün yararı gözetilerek velayet ve aile bireyleriyle ilişki düzenlemelerinin yapılması.']]},
  {name:'İş Hukuku',desc:'İşçi ve işveren arasındaki ilişkilerden doğan uyuşmazlıklarda danışmanlık ve dava takibi.',tags:['Kıdem & ihbar tazminatı','İşe iade','Fazla mesai alacakları','Mobbing & hizmet tespiti'],
   nedir:'İş Hukuku Avukatı Nedir?',
   ned:'İş hukuku avukatı, işçi ve işveren arasındaki ilişkilerden doğan uyuşmazlıklarda hukuki destek sağlayan avukattır. Kıdem ve ihbar tazminatı, işe iade, fazla mesai alacakları, mobbing ve sosyal güvenlik uyuşmazlıkları gibi konularda hem işçilere hem işverenlere danışmanlık ve dava takibi hizmeti sunar.',
   steps:[['Hizmet süresi ve alacakların hesaplanması','Kıdem, ihbar tazminatı ve işçilik alacaklarının mevzuata uygun hesaplanması ve talep edilmesi.'],['İşe iade davası açılması','Haksız fesih durumunda işe iade veya tazminat talebiyle dava açılması ve yürütülmesi.'],['Arabuluculuk sürecinin yönetimi','Zorunlu arabuluculuk sürecinde müvekkil adına müzakerelerin profesyonel olarak yürütülmesi.'],['Sosyal güvenlik uyuşmazlıklarının takibi','SGK prim borçları, hizmet tespiti ve kayıt dışı çalışmaya ilişkin davaların takibi.']]},
  {name:'Gayrimenkul ve Kira Hukuku',desc:'Taşınmazlara ilişkin uyuşmazlıklarda danışmanlık ve dava takibi; tapudan kira ilişkilerine.',tags:['Tahliye & kira tespiti','Tapu iptal ve tescil','Ortaklığın giderilmesi','İnşaat sözleşmeleri'],
   nedir:'Gayrimenkul Avukatı Nedir?',
   ned:'Gayrimenkul ve kira hukuku avukatı, taşınmazlara ilişkin hukuki uyuşmazlıklarda danışmanlık ve dava takibi hizmeti sunan avukattır. Tapu iptal ve tescil, tahliye, kira tespit, ortaklığın giderilmesi ve inşaat sözleşmelerinden doğan uyuşmazlıklar bu alanın başlıca konularındandır.',
   steps:[['Tapu iptal ve tescil davası açılması','Hatalı veya haksız tapuya karşı iptal davası açılması ve tescil işlemlerinin takibi.'],['Kira tahliyesi ve tespit davası','Kiracının tahliyesi veya kira bedelinin tespiti için dava açılması ve yürütülmesi.'],['Kat mülkiyeti ve site yönetimi uyuşmazlıkları','Apartman ve site yönetiminden doğan hukuki sorunların çözümü.'],['İnşaat ve müteahhitlik sözleşmelerinin hazırlanması','Tarafların haklarını koruyacak sözleşmelerin hazırlanması ve uyuşmazlık yönetimi.']]},
  {name:'İdare Hukuku',desc:'Bireylerin ve kurumların kamu idaresiyle yaşadığı uyuşmazlıklarda hukuki destek.',tags:['İptal & tam yargı davaları','Kamu görevlileri','Kamulaştırma','Belediye ve imar'],
   nedir:'İdare Hukuku Avukatı Nedir?',
   ned:'İdare hukuku avukatı, bireylerin ve kurumların kamu idaresiyle yaşadığı uyuşmazlıklarda hukuki destek sağlayan avukattır. İdari işlemlerin iptali, tam yargı davaları, kamulaştırma, imar uyuşmazlıkları ve kamu görevlileriyle ilgili davalar bu alanın temel konularını oluşturur.',
   steps:[['İdari işlemin iptali için dava açılması','Hukuka aykırı idari kararların iptali amacıyla idare mahkemesinde dava açılması.'],['Tam yargı davası ve tazminat talebi','İdarenin eylem veya işleminden doğan zararın tazmini için tam yargı davası açılması.'],['Kamulaştırma bedel tespiti','Kamulaştırma kararlarına itiraz ve bedel artırımı davalarının yürütülmesi.'],['İmar ve ruhsat uyuşmazlıklarının çözümü','İmar planı değişiklikleri ve ruhsat iptallerinden doğan davaların takibi.']]},
  {name:'İcra ve İflas Hukuku',desc:'Alacak takibi, borç tahsilatı ve iflas süreçlerinde alacaklı veya borçlu adına hukuki destek.',tags:['İlamlı & ilamsız icra','İhtiyati haciz','Çek & senet takibi','İtirazın iptali'],
   nedir:'İcra ve İflas Avukatı Nedir?',
   ned:'İcra ve iflas hukuku avukatı, alacak takibi, borç tahsilatı ve iflas süreçlerinde alacaklı veya borçlu adına hukuki destek sağlayan avukattır. İlamlı ve ilamsız icra takiplerinden ihtiyati hacze, çek-senet takiplerinden konkordatoya kadar geniş bir alanda hizmet sunar.',
   steps:[['İcra takibi başlatılması','Alacağın tahsili için ilamsız veya ilamlı icra takibi başlatılması ve yönetilmesi.'],['İhtiyati haciz kararı alınması','Borçlunun mal kaçırmasını önlemek amacıyla ihtiyati haciz kararı için mahkemeye başvurulması.'],['İtirazın iptali ve kaldırılması','Borçlunun icra takibine itirazına karşı iptal davası veya itirazın kaldırılması yoluna başvurulması.'],['İflas ve konkordato süreçlerinin takibi','Şirketin ya da kişinin iflas veya konkordato sürecinin hukuki olarak yönetilmesi.']]},
  {name:'Tüketici Hukuku',desc:'Tüketicilerin satın aldıkları mal ve hizmetlerden kaynaklanan uyuşmazlıklarda hak takibi.',tags:['Hakem heyeti süreçleri','Tüketici mahkemesi','Araç değer kaybı','Ayıplı mal ve hizmet'],
   nedir:'Tüketici Hukuku Avukatı Nedir?',
   ned:'Tüketici hukuku avukatı, tüketicilerin satın aldıkları mal ve hizmetlerden kaynaklanan uyuşmazlıklarda haklarını koruyan avukattır. Ayıplı ürün, haksız sözleşme şartları, araç değer kaybı ve tüketici mahkemesi süreçleri bu alanın başlıca konularındandır.',
   steps:[['Tüketici hakem heyetine başvuru','Uyuşmazlığın tutarına göre tüketici hakem heyetine başvurunun hazırlanması ve takibi.'],['Tüketici mahkemesinde dava açılması','Hakem heyeti kararına itiraz veya doğrudan tüketici mahkemesinde dava açılması.'],['Ayıplı mal ve hizmet iade/tazminat talebi','Ayıplı ürün veya hizmet nedeniyle iade, değişim ya da tazminat talebinin yürütülmesi.'],['Araç değer kaybı hesaplama ve başvuru','Trafik kazası sonrası oluşan araç değer kaybının hesaplanması ve sigortaya karşı talep edilmesi.']]},
  {name:'Ticaret Hukuku',desc:'Şirketler, ticari ilişkiler ve iş ortaklıklarından doğan uyuşmazlıklarda danışmanlık ve dava.',tags:['Şirket kuruluşu','Ticari sözleşmeler','Ortaklık anlaşmazlıkları','Sürekli danışmanlık'],
   nedir:'Ticaret Hukuku Avukatı Nedir?',
   ned:'Ticaret hukuku avukatı, şirketler, ticari ilişkiler ve iş ortaklıklarından doğan hukuki uyuşmazlıklarda danışmanlık ve dava hizmeti sunan avukattır. Şirket kuruluşu, ticari sözleşmelerin hazırlanması, ortaklık anlaşmazlıkları ve ticari dava takibi bu alanın temel konuları arasında yer alır.',
   steps:[['Şirket kuruluşu ve sözleşmelerin hazırlanması','Şirket türüne uygun ana sözleşme ve ticari sözleşmelerin hukuki olarak hazırlanması.'],['Ortaklık uyuşmazlıklarının çözümü','Ortaklar arasındaki anlaşmazlıkların müzakere veya dava yoluyla çözüme kavuşturulması.'],['Ticari alacak takibi','Şirketin alacaklarının icra veya dava yoluyla tahsil edilmesi.'],['Sürekli hukuki danışmanlık','Şirketin günlük ticari faaliyetlerine ilişkin hukuki risklerin değerlendirilmesi ve yönetilmesi.']]},
  {name:'Yabancılar Hukuku',desc:'Yabancı uyruklu bireylerin oturma, çalışma izni, vatandaşlık ve sınır dışı süreçlerinde destek.',tags:['İkamet & çalışma izni','Türk vatandaşlığı','Deport kararının iptali','Tanıma ve tenfiz'],
   nedir:'Yabancılar Hukuku Avukatı Nedir?',
   ned:'Yabancılar hukuku avukatı, Türkiye’de yaşayan veya yaşamak isteyen yabancı uyruklu bireylerin oturma izni, çalışma izni, vatandaşlık başvuruları ve sınır dışı etme gibi konularda hukuki destek sağlayan avukattır. Uluslararası koruma talepleri ve yabancı mahkeme kararlarının tanınması da bu alanın kapsamındadır.',
   steps:[['İkamet ve çalışma izni başvurularının hazırlanması','Türkiye’de yasal statü kazanmak için gerekli başvuruların eksiksiz hazırlanması ve takibi.'],['Türk vatandaşlığı başvurusu','Olağan veya istisnai vatandaşlık başvurularının hazırlanması ve sürecin yönetilmesi.'],['Sınır dışı (deport) kararına itiraz','Sınır dışı etme kararına karşı idare mahkemesinde itiraz davası açılması.'],['Tanıma ve tenfiz davaları','Yabancı mahkeme ve tahkim kararlarının Türkiye’de geçerli kılınması için dava açılması.']]}
];

(function(){
  const areasEl=document.getElementById('areas');
  if(!areasEl)return;
  AREAS.forEach((a,i)=>{
    const el=document.createElement('div');
    el.className='area';
    el.id='alan-'+(i+1);
    el.innerHTML=`
      <div class="area-top">
        <div class="area-no">${String(i+1).padStart(2,'0')}</div>
        <div class="area-name">${a.name}</div>
        <div class="area-plus"></div>
      </div>
      <div class="area-body"><div class="area-body-inner">
        <div class="area-detail">
          <div class="ad-spacer"></div>
          <div class="ad-main">
            <p class="ad-desc">${a.desc}</p>
            <ul class="area-tags">${a.tags.map(t=>`<li>${t}</li>`).join('')}</ul>
            <div class="ad-nedir">${a.nedir}</div>
            <p class="ad-nedir-p">${a.ned}</p>
            <div class="ad-steps">
              ${a.steps.map((s,n)=>`<div class="ad-step"><div class="sn">${n+1}</div><div><div class="st">${s[0]}</div><div class="sd">${s[1]}</div></div></div>`).join('')}
            </div>
            <a class="btn-solid ad-cta" href="/iletisim">Bu alanda randevu al
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            </a>
          </div>
        </div>
      </div></div>`;
    el.querySelector('.area-top').addEventListener('click',()=>{
      const open=el.classList.contains('open');
      document.querySelectorAll('.area.open').forEach(o=>o.classList.remove('open'));
      if(!open)el.classList.add('open');
    });
    el.querySelectorAll('.ad-main a').forEach(x=>x.addEventListener('click',e=>e.stopPropagation()));
    areasEl.appendChild(el);
  });
  const h=location.hash;
  if(h&&/^#alan-[1-9]$/.test(h)){
    const t=document.getElementById(h.slice(1));
    if(t){
      t.classList.add('open');
      setTimeout(()=>window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-90,behavior:'smooth'}),240);
    }
  }
})();

/* ───────────── articles ───────────── */
const ARTICLES=[
  {dal:'Aile Hukuku',baslik:'Boşanma davalarında af sayılan haller',ozet:'Yargıtay kararları ışığında eşin kusurlu davranışını bilmesine rağmen evlilik birliğini sürdürme iradesinin sonuçları.',url:'https://www.hukukihaber.net/yargitay-kararlari-cercevesinde-bosanma-davalarinda-af-sayilan-ve-sayilmayan-haller-1'},
  {dal:'Aile Hukuku',baslik:'Aile konutu üzerinde tasarruf işlemleri',ozet:'TMK m.194 kapsamında aile konutunun devri, ipoteği ve kira sözleşmesinin feshi için eş rızası.',url:'https://www.hukukihaber.net/turk-medeni-kanunu-m-194-kapsaminda-aile-konutu-uzerinde-yapilan-tasarruf-islemleri'},
  {dal:'Aile Hukuku',baslik:'Velayet davalarında çocuğun üstün yararı',ozet:'Velayet kararlarında çocuğun yaşı, gelişimi ve ebeveyn koşullarının mahkemece değerlendirilme ölçütleri.',url:'https://dergipark.org.tr/tr/search?q=velayet+%C3%BCst%C3%BCn+yarar'},
  {dal:'İş Hukuku',baslik:'İş sözleşmelerinde cezai şart',ozet:'İş sözleşmelerinde karşılıklılık ilkesi ve yalnızca işçi aleyhine düzenlenen cezai şartların geçerliliği.',url:'https://www.hukukihaber.net/is-sozlesmelerinde-cezai-sart-aleyna-yilmaz'},
  {dal:'İş Hukuku',baslik:'İşe iade davasında fesih bildiriminin şekli şartları',ozet:'Yazılı bildirim zorunluluğu, fesih gerekçesinin somutlaştırılması ve bu eksikliklerin dava sonucuna etkisi.',url:'https://dergipark.org.tr/tr/search?q=i%C5%9Fe+iade+fesih+bildirimi'},
  {dal:'İş Hukuku',baslik:'Kıdem tazminatında esas ücretin kapsamı',ozet:'Sürekli ödeme niteliğindeki yan ödemelerin esas ücrete dahil edilmesine ilişkin Yargıtay kriterleri.',url:'https://dergipark.org.tr/tr/search?q=k%C4%B1dem+tazminat%C4%B1+%C3%BCcret+hesap'},
  {dal:'Gayrimenkul Hukuku',baslik:'Kira bedelinin tespiti davasında ıslah',ozet:'Kira tespit davalarında talep sonucunun artırılması ve dava öncesi emsal kira analizinin önemi.',url:'https://www.hukukihaber.net/kira-bedelinin-tespiti-davasinda-talep-sonuc-islah-edilebilir-mi'},
  {dal:'Gayrimenkul Hukuku',baslik:'Tapu iptali ve tescil davalarında zamanaşımı',ozet:'Muvazaalı satışlar ile inançlı işlemlere dayanan tapu iptal davalarında dava hakkının zamanla sınırlandırılması.',url:'https://dergipark.org.tr/tr/search?q=tapu+iptal+tescil+zaman a%C5%9F%C4%B1m%C4%B1'},
  {dal:'Gayrimenkul Hukuku',baslik:'Kat karşılığı inşaat sözleşmesinde arsa sahibinin temerrüdü',ozet:'Arsa sahibinin teslim yükümlülüğünü yerine getirmemesi hâlinde müteahhidin seçimlik hakları.',url:'https://dergipark.org.tr/tr/search?q=kat+kar%C5%9F%C4%B1l%C4%B1%C4%9F%C4%B1+in%C5%9Faat+s%C3%B6zle%C5%9Fmesi'},
  {dal:'Ceza Hukuku',baslik:'Haksız tahrik indiriminin uygulanma koşulları',ozet:'TCK m.29 kapsamında tahriki doğuran eylemin haksızlığı, orantılılık ve Yargıtay’ın güncel yorumu.',url:'https://dergipark.org.tr/tr/search?q=haks%C4%B1z+tahrik+indirimi+TCK'},
  {dal:'Ceza Hukuku',baslik:'Bilişim suçlarında dijital delil ve hukuka uygunluk',ozet:'Cihaz incelemesi, log kayıtları ve sosyal medya verilerinin delil değeri ile elde edilme usulünün önemi.',url:'https://dergipark.org.tr/tr/search?q=bili%C5%9Fim+su%C3%A7+dijital+delil'},
  {dal:'Ceza Hukuku',baslik:'Uyuşturucu suçlarında etkin pişmanlık',ozet:'TCK m.192 uyarınca gönüllü vazgeçme, yetkililere bildirme ve katkının ceza indirimini doğurma koşulları.',url:'https://dergipark.org.tr/tr/search?q=etkin+pi%C5%9Fmanl%C4%B1k+uyu%C5%9Fturucu+TCK'},
  {dal:'İdare Hukuku',baslik:'İptal davalarında yürütmenin durdurulması',ozet:'İdare mahkemelerinin YD kararı verebilmesi için aranan açık hukuka aykırılık ve telafisi güç zarar koşulları.',url:'https://dergipark.org.tr/tr/search?q=y%C3%BCr%C3%BCtmenin+durdurulmas%C4%B1+ko%C5%9Ful'},
  {dal:'İdare Hukuku',baslik:'Kamulaştırmasız el koymada bedel tespiti',ozet:'Fiili el koyma hâlinde mülk sahibinin bedel tespiti davası, kademeli faiz ve mevduat faizinin uygulanması.',url:'https://dergipark.org.tr/tr/search?q=kamula%C5%9Ft%C4%B1rmas%C4%B1z+el+koyma+tazminat'},
  {dal:'İdare Hukuku',baslik:'Disiplin cezalarına karşı idari yargı yolları',ozet:'Kamu görevlilerine verilen disiplin cezalarının iptali için başvuru süreleri ve yargısal denetimin sınırları.',url:'https://dergipark.org.tr/tr/search?q=disiplin+cezas%C4%B1+iptal+davas%C4%B1'},
  {dal:'İcra Hukuku',baslik:'İhtiyati haciz kararlarına itiraz',ozet:'Haksız veya eksik evrakla alınan ihtiyati haciz kararlarına karşı izlenecek kısa süreli itiraz yolları.',url:'https://dergipark.org.tr/tr/search?q=%22ihtiyati+haciz%22'},
  {dal:'İcra Hukuku',baslik:'Menfi tespit davasında takibin iptali ve tazminat',ozet:'Borçlunun haksız icra takibine karşı %20 inkâr tazminatı isteme hakkı ve davanın açılma zamanlaması.',url:'https://dergipark.org.tr/tr/search?q=menfi+tespit+inkar+tazminat%C4%B1'},
  {dal:'İcra Hukuku',baslik:'Kambiyo takibinde zamanaşımı def’i',ozet:'Çek ve bonoya dayalı kambiyo senetleri takibinde zamanaşımının re’sen gözetilme sınırları ve itiraz usulü.',url:'https://dergipark.org.tr/tr/search?q=icra+zaman a%C5%9F%C4%B1m%C4%B1+kambiyo'},
  {dal:'Yabancılar Hukuku',baslik:'Sınır dışı kararları ve itiraz yolları',ozet:'Göç İdaresi tarafından verilen deport kararlarına karşı idari yargıda başvuru süreci.',url:'https://dergipark.org.tr/tr/search?q=%22s%C4%B1n%C4%B1r+d%C4%B1%C5%9F%C4%B1+karar%C4%B1%22'},
  {dal:'Yabancılar Hukuku',baslik:'Oturma izni iptalinde idari itiraz süreci',ozet:'Kısa dönem ve aile ikamet izinlerinin iptalinde bildirim zorunluluğu, itiraz süreleri ve yargı yolu.',url:'https://dergipark.org.tr/tr/search?q=oturma+izni+iptali+itiraz'},
  {dal:'Yabancılar Hukuku',baslik:'Yabancıların taşınmaz edinmesinde yasal kısıtlar',ozet:'Mütekabiliyet ilkesi, askeri yasak bölgeler ve izin gerektiren alanlarda tapu tescili süreci.',url:'https://dergipark.org.tr/tr/search?q=yabanc%C4%B1+ta%C5%9F%C4%B1nmaz+edinme'}
];

(function(){
  const grid=document.getElementById('artGrid');
  if(!grid)return;
  const filter=document.getElementById('artFilter');
  const limit=parseInt(grid.dataset.limit||'0',10);
  function render(f){
    grid.innerHTML='';
    let list=ARTICLES.filter(a=>f==='Tümü'||a.dal===f);
    if(limit>0)list=list.slice(0,limit);
    list.forEach(a=>{
      const el=document.createElement('a');
      el.className='art';el.href=a.url;el.target='_blank';el.rel='noopener';
      el.innerHTML=`<span class="art-tag">${a.dal}</span><h4>${a.baslik}</h4><p>${a.ozet}</p><span class="art-read">Yazıyı oku →</span>`;
      grid.appendChild(el);
    });
  }
  if(filter){
    const dallar=['Tümü',...new Set(ARTICLES.map(a=>a.dal))];
    dallar.forEach((d,i)=>{
      const c=document.createElement('button');
      c.className='art-chip'+(i===0?' on':'');
      c.textContent=d;
      c.addEventListener('click',()=>{
        filter.querySelectorAll('.art-chip').forEach(x=>x.classList.remove('on'));
        c.classList.add('on');render(d);
      });
      filter.appendChild(c);
    });
  }
  render('Tümü');
})();

/* ───────────── faq ───────────── */
const FAQS=[
  {q:"Antalya'da boşanma davası nasıl açılır?",a:'Boşanma davası, eşlerden birinin son altı aydır oturduğu veya eşlerin son altı aydır birlikte oturdukları yer aile mahkemesinde açılır. Anlaşmalı boşanmada ortak bir protokol hazırlanırken, çekişmeli boşanmada dava dilekçesi ve deliller hukuki stratejiye göre düzenlenir.'},
  {q:'Ceza davalarında avukat tutmak zorunlu mudur?',a:'Kural olarak zorunlu değildir; ancak alt sınırı beş yıldan fazla hapis cezası gerektiren suçlarda ve bazı hallerde mahkeme zorunlu müdafi atar. Soruşturmanın ilk aşamasından itibaren avukatla çalışmak, hak kayıplarının önüne geçer.'},
  {q:'Avukatlık ücreti neye göre belirlenir?',a:'Ücret; işin niteliği, kapsamı, harcanacak emek ve süre ile Avukatlık Asgari Ücret Tarifesi dikkate alınarak belirlenir. Görüşme öncesi şeffaf bir ücretlendirme sunulur ve sözleşmeyle netleştirilir.'},
  {q:'Online hukuki danışmanlık veriliyor mu?',a:'Evet. Yüz yüze görüşmenin yanı sıra telefon ve çevrim içi görüşme seçenekleri sunulmaktadır. Şehir dışında bulunan müvekkiller için dosya süreci çevrim içi de yürütülebilir.'},
  {q:'Yabancılar Türkiye’de gayrimenkul satın alabilir mi?',a:'Belirli ülke vatandaşları için kısıtlamalar bulunsa da yabancılar, askeri ve güvenlik bölgeleri dışında kalan taşınmazları edinebilir. Tapu işlemleri öncesi hukuki inceleme, ileride doğabilecek uyuşmazlıkları önler.'},
  {q:'İcra takibinde süreler neden önemlidir?',a:'İcra ve iflas hukukunda itiraz, şikâyet ve dava açma süreleri kesindir; kaçırılması ciddi hak kayıplarına yol açar. Bu nedenle tebligatın ardından vakit kaybetmeden hukuki destek alınması önerilir.'}
];

(function(){
  const faqEl=document.getElementById('faq');
  if(!faqEl)return;
  FAQS.forEach((f,i)=>{
    const el=document.createElement('div');
    el.className='qa';
    el.innerHTML=`
      <button class="qa-q">
        <span class="qa-mark">0${i+1}</span>
        <span>${f.q}</span>
        <span class="qa-ico"></span>
      </button>
      <div class="qa-a"><div class="qa-a-inner"><p>${f.a}</p></div></div>`;
    el.querySelector('.qa-q').addEventListener('click',()=>{
      const open=el.classList.contains('open');
      document.querySelectorAll('.qa.open').forEach(o=>o.classList.remove('open'));
      if(!open)el.classList.add('open');
    });
    faqEl.appendChild(el);
  });
})();

/* ───────────── scroll reveal ───────────── */
(function(){
  const els=document.querySelectorAll('.rv');
  if(!els.length)return;
  const io=new IntersectionObserver(es=>{
    es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});
  },{threshold:.12});
  els.forEach(el=>io.observe(el));
})();
