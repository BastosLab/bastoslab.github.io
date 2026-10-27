// Renders window.PROJECTS into #cards. Uses textContent only (no HTML injection).
const el=(t,c,x)=>{const e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e};
const root=document.getElementById("cards");
for(const p of window.PROJECTS){
  const a=el("a","card");a.href=p.url;a.rel="noopener";
  a.append(el("h3",null,p.name),el("p",null,p.description));
  const t=el("div","tags");for(const g of p.tags||[])t.append(el("span","tag",g));
  a.append(t,el("span","go","Open site →"));
  root.append(a);
}
