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
  {name:'Criminal Law',desc:'Protecting the rights of individuals facing criminal charges throughout the investigation and prosecution stages.',tags:['Serious felony & misdemeanor','Objection to detention','Cybercrime','Traffic accident criminal cases'],
   nedir:'What is a Criminal Defense Attorney?',
   ned:'A criminal defense attorney protects the legal rights of individuals facing criminal charges during investigation and prosecution stages. They provide defense services throughout the entire criminal proceedings, from the suspect or accused giving testimony to objecting to detention, from the trial process to the appeal stage.',
   steps:[['Representation during testimony and interrogation','Management of the testimony process while protecting the client’s rights at law enforcement and prosecutor stage.'],['Objection to detention and judicial control decisions','Preparation of objection petitions against unjust detention or judicial control decisions.'],['Preparation of trial defense','Strategic conduct of evidence evaluation, witness examination and court defense.'],['Appeal and legal remedy applications','Preparation of appeal and Supreme Court applications against first-instance court decisions.']]},
  {name:'Real Estate & Tenancy Law',desc:'Consultation and litigation in disputes related to immovable property; from title deeds to tenancy relations.',tags:['Eviction & rent determination','Title deed cancellation','Dissolution of co-ownership','Construction contracts'],
   nedir:'What is a Real Estate Attorney?',
   ned:'A real estate and tenancy law attorney provides consultation and litigation services in legal disputes related to immovable properties. Title deed cancellation and registration, eviction, rent determination, dissolution of co-ownership and disputes from construction contracts are the main topics of this field.',
   steps:[['Filing title deed cancellation and registration lawsuit','Filing a cancellation lawsuit against an erroneous or wrongful title deed and following up registration proceedings.'],['Tenant eviction and rent determination lawsuit','Filing and conducting a lawsuit for eviction of tenant or determination of rent amount.'],['Condominium and site management disputes','Resolution of legal issues arising from apartment and residential complex management.'],['Preparation of construction and contracting agreements','Preparation of contracts that protect the rights of the parties and dispute management.']]},
  {name:'Employment Law',desc:'Consultation and litigation in disputes arising from employer-employee relationships.',tags:['Severance & notice pay','Reinstatement','Overtime receivables','Harassment & service determination'],
   nedir:'What is an Employment Law Attorney?',
   ned:'An employment law attorney provides legal support in disputes arising from employer-employee relationships. They offer consultation and litigation services to both employees and employers on severance and notice pay, reinstatement, overtime wages, workplace harassment and social security disputes.',
   steps:[['Calculation of service period and claims','Calculation and claim of severance pay, notice pay and employment receivables in accordance with legislation.'],['Filing a reinstatement lawsuit','Filing and conducting a lawsuit for reinstatement or compensation in the event of unjust termination.'],['Managing the mediation process','Professional conduct of negotiations on behalf of the client in mandatory mediation proceedings.'],['Follow-up of social security disputes','Follow-up of cases related to social security premium debts, service determination and informal employment.']]},
  {name:'Family Law',desc:'Legal support to parties in disputes arising from family relationships such as marriage, divorce, custody, alimony and property division.',tags:['Contested & uncontested divorce','Alimony and custody','Property division','Recognition and enforcement'],
   nedir:'What is a Family Law Attorney?',
   ned:'A family law attorney provides legal support to parties in disputes arising from family relationships such as marriage, divorce, custody, alimony and property division. Family cases are not limited to the dissolution of marriage; they also cover child custody, alimony, dissolution of the matrimonial property regime and compensation.',
   steps:[['Preparation of divorce petition','Preparation of a complete petition in accordance with the legal strategy of the case and submission to the court.'],['Collection and presentation of evidence','Professional compilation of evidence that will determine the course of the case and presentation in court.'],['Preparation of alimony and compensation claims','Determination and follow-up of alimony and compensation claims appropriate to the client’s rights.'],['Custody and personal relationship arrangements','Making custody and family member relationship arrangements in the best interests of the child.']]},
  {name:'Administrative Law',desc:'Legal support to individuals and institutions in disputes with public administration.',tags:['Annulment & full remedy','Disputes with civil servants','Expropriation','Municipality and zoning'],
   nedir:'What is an Administrative Law Attorney?',
   ned:'An administrative law attorney provides legal support to individuals and institutions in disputes with public administration. Annulment of administrative acts, full remedy lawsuits, expropriation, zoning disputes and cases related to civil servants are the fundamental topics of this field.',
   steps:[['Filing lawsuit for annulment of administrative act','Filing a lawsuit in administrative court for annulment of unlawful administrative decisions.'],['Full remedy lawsuit and compensation claim','Filing a full remedy lawsuit for compensation of damages arising from the administration’s actions or transactions.'],['Expropriation price determination','Objection to expropriation decisions and conduct of price increase lawsuits.'],['Resolution of zoning and permit disputes','Follow-up of cases arising from zoning plan changes and permit cancellations.']]},
  {name:'Enforcement & Bankruptcy Law',desc:'Legal support for creditors or debtors in debt collection and bankruptcy proceedings.',tags:['Judgment-based & non-judgment enforcement','Precautionary attachment','Check & promissory note','Cancellation of objection'],
   nedir:'What is an Enforcement & Bankruptcy Attorney?',
   ned:'An enforcement and bankruptcy law attorney provides legal support on behalf of creditors or debtors in debt collection and bankruptcy proceedings. They serve across a wide range from judgment-based and non-judgment enforcement to precautionary attachment, from check-promissory note follow-up to concordat.',
   steps:[['Initiating enforcement proceedings','Initiating and managing non-judgment or judgment-based enforcement proceedings for debt collection.'],['Obtaining precautionary attachment order','Applying to court for precautionary attachment order to prevent the debtor from concealing assets.'],['Cancellation and removal of objection','Filing a cancellation lawsuit or applying for removal of objection against the debtor’s objection to enforcement.'],['Follow-up of bankruptcy and concordat proceedings','Legal management of the company’s or individual’s bankruptcy or concordat proceedings.']]},
  {name:'Consumer Law',desc:'Protecting consumer rights in disputes arising from goods and services purchased.',tags:['Arbitration committee','Consumer court','Vehicle depreciation','Defective goods and services'],
   nedir:'What is a Consumer Law Attorney?',
   ned:'A consumer law attorney protects the rights of consumers in disputes arising from goods and services they purchase. Defective products, unfair contract terms, vehicle depreciation and consumer court processes are the main topics of this field.',
   steps:[['Application to consumer arbitration committee','Preparation and follow-up of the application to the consumer arbitration committee according to the amount of the dispute.'],['Filing lawsuit in consumer court','Filing a lawsuit in consumer court against the arbitration committee decision or directly.'],['Defective goods and service refund/compensation claim','Conducting refund, replacement or compensation claims due to defective product or service.'],['Vehicle depreciation calculation and application','Calculation of vehicle depreciation after traffic accident and claiming against insurance.']]},
  {name:'Commercial Law',desc:'Consultation and litigation in disputes arising from companies, commercial relations and business partnerships.',tags:['Company formation','Commercial contracts','Partnership disputes','Ongoing consultation'],
   nedir:'What is a Commercial Law Attorney?',
   ned:'A commercial law attorney provides consultation and litigation services in legal disputes arising from companies, commercial relations and business partnerships. Company formation, preparation of commercial contracts, partnership disputes and commercial litigation follow-up are among the fundamental topics of this field.',
   steps:[['Company formation and contract preparation','Legal preparation of articles of association and commercial contracts appropriate to the type of company.'],['Resolution of partnership disputes','Resolution of disputes between partners through negotiation or litigation.'],['Commercial debt collection','Collection of company receivables through enforcement or litigation.'],['Ongoing legal consultation','Evaluation and management of legal risks related to the company’s daily commercial activities.']]},
  {name:'Immigration Law',desc:'Legal support to foreign nationals on residence, work permits, citizenship and deportation matters.',tags:['Residence & work permit','Turkish citizenship','Deportation cancellation','Recognition & enforcement'],
   nedir:'What is an Immigration Law Attorney?',
   ned:'An immigration law attorney provides legal support to foreign nationals living or wishing to live in Turkey on matters such as residence permits, work permits, citizenship applications and deportation. International protection claims and recognition of foreign court decisions are also within the scope of this field.',
   steps:[['Preparation of residence and work permit applications','Complete preparation and follow-up of necessary applications to obtain legal status in Turkey.'],['Turkish citizenship application','Preparation of ordinary or exceptional citizenship applications and management of the process.'],['Objection to deportation decision','Filing an objection lawsuit in administrative court against the deportation decision.'],['Recognition and enforcement lawsuits','Filing a lawsuit to make foreign court and arbitration decisions valid in Turkey.']]}
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
            <a class="btn-solid ad-cta" href="/en/iletisim">Book an appointment
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
  {dal:'Family Law',baslik:'Forgiveness in Divorce Cases',ozet:"Consequences of continuing the marriage despite knowing the spouse's fault, in the light of Supreme Court decisions.",url:'https://www.hukukihaber.net/yargitay-kararlari-cercevesinde-bosanma-davalarinda-af-sayilan-ve-sayilmayan-haller-1'},
  {dal:'Family Law',baslik:'Transactions over the Family Residence',ozet:'Spousal consent required for the transfer, mortgage and termination of the tenancy of the family residence under Article 194 of the Turkish Civil Code.',url:'https://www.hukukihaber.net/turk-medeni-kanunu-m-194-kapsaminda-aile-konutu-uzerinde-yapilan-tasarruf-islemleri'},
  {dal:'Employment Law',baslik:'Penalty Clauses in Employment Contracts',ozet:'The reciprocity principle in employment contracts and the validity of penalty clauses arranged solely against the employee.',url:'https://www.hukukihaber.net/is-sozlesmelerinde-cezai-sart-aleyna-yilmaz'},
  {dal:'Real Estate Law',baslik:'Amendment of Claims in Rent Determination Cases',ozet:'Increasing the claim amount in rent determination cases and the importance of comparable rent analysis before the lawsuit.',url:'https://www.hukukihaber.net/kira-bedelinin-tespiti-davasinda-talep-sonuc-islah-edilebilir-mi'},
  {dal:'Enforcement & Bankruptcy Law',baslik:'Objection to Precautionary Attachment Orders',ozet:'Short-term objection routes against precautionary attachment decisions obtained unlawfully or with incomplete documentation.',url:'https://dergipark.org.tr/tr/search?q=%22ihtiyati+haciz%22'},
  {dal:'Immigration Law',baslik:'Deportation Decisions and Objection Procedures',ozet:'Application process in administrative courts against deportation decisions issued by the Immigration Administration.',url:'https://dergipark.org.tr/tr/search?q=%22s%C4%B1n%C4%B1r+d%C4%B1%C5%9F%C4%B1+karar%C4%B1%22'}
];
(function(){
  const grid=document.getElementById('artGrid');
  if(!grid)return;
  const filter=document.getElementById('artFilter');
  const limit=parseInt(grid.dataset.limit||'0',10);
  function render(f){
    grid.innerHTML='';
    let list=ARTICLES.filter(a=>f==='All'||a.dal===f);
    if(limit>0)list=list.slice(0,limit);
    list.forEach(a=>{
      const el=document.createElement('a');
      el.className='art';el.href=a.url;el.target='_blank';el.rel='noopener';
      el.innerHTML=`<span class="art-tag">${a.dal}</span><h4>${a.baslik}</h4><p>${a.ozet}</p><span class="art-read">Read article →</span>`;
      grid.appendChild(el);
    });
  }
  if(filter){
    const dallar=['All',...new Set(ARTICLES.map(a=>a.dal))];
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
  render('All');
})();

/* ───────────── faq ───────────── */
const FAQS=[
  {q:'How is a divorce case filed in Antalya?',a:'A divorce case is filed in the Family Court at the domicile of either spouse. An uncontested divorce requires at least one year of marriage and a settlement agreement; in contested cases, fault, alimony, custody, property division and compensation claims are evaluated separately.'},
  {q:'Is hiring a lawyer mandatory in criminal cases?',a:'It is not mandatory in every case; however, it is required to appoint a defense attorney in crimes carrying a minimum sentence of more than five years imprisonment and in certain special circumstances. Establishing the defense from the investigation stage onward is critically important.'},
  {q:'How are attorney fees determined?',a:'Fees are determined by written agreement based on the type, scope, duration and workload of the case, not falling below the Minimum Attorney Fee Schedule published by the Turkish Bar Association.'},
  {q:'Is online legal consultation available?',a:'Yes. For matters requiring file review, documents can be forwarded digitally; consultations can be conducted via phone or video conference.'},
  {q:'Can foreigners purchase real estate in Turkey?',a:'Yes, with certain restrictions. Legal review before any transaction is necessary regarding military prohibited zones, area limitations and citizenship application eligibility.'},
  {q:'Why are deadlines critical in enforcement proceedings?',a:'In enforcement and attachment proceedings, the deadlines for objection, payment orders, precautionary attachment and litigation are extremely short and can result in loss of rights. A prompt legal assessment must be made upon receipt of service of process.'}
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
