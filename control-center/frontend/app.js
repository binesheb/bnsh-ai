const API="http://127.0.0.1:8790";
const modelsRoot=document.getElementById("models");
const cpu=document.getElementById("cpu");
const memory=document.getElementById("memory");

async function api(path){const r=await fetch(API+path);if(!r.ok)throw new Error(await r.text());return r.json()}

async function load(){
  try{
    const [sys,cat,activity]=await Promise.all([api("/api/system"),api("/api/models"),api("/api/activity")]);
    cpu.textContent=sys.cpu||"—";
    memory.textContent=sys.memory||"—";
    modelsRoot.innerHTML=cat.models.map(m=>`
      <div class="model">
        <div><h4>${m.name}</h4><p>${m.description} · ${m.status}</p></div>
        <button class="install" data-id="${m.id}" ${m.status==="planned"?"disabled":""}>${m.status==="planned"?"Planned":"Install"}</button>
      </div>`).join("");
    document.querySelector(".activity").innerHTML=activity.items.map(x=>`<div><b>${x.name}</b><span>${x.status}</span></div>`).join("");
  }catch(err){
    cpu.textContent="Offline";
    memory.textContent="API unavailable";
    modelsRoot.innerHTML='<div class="model"><div><h4>Control API unavailable</h4><p>Start BNSH Control to connect the dashboard.</p></div></div>';
  }
}
load();
setInterval(load,5000);
