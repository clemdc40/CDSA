document.addEventListener('DOMContentLoaded', () => {
  const search = document.querySelector('input[data-md-component="search-query"]');
  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement !== search) {
      e.preventDefault();
      search.focus();
    }
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      search.focus();
    }
  });

  const copyBtn = document.createElement('button');
  copyBtn.id = 'copy-all';
  copyBtn.textContent = 'Copy all commands';
  copyBtn.addEventListener('click', () => {
    const blocks = Array.from(document.querySelectorAll('pre code'));
    const text = blocks.map(b => b.innerText).join('\n');
    navigator.clipboard.writeText(text);
  });
  const content = document.querySelector('.md-content');
  if (content) content.prepend(copyBtn);

  fetch('/overrides/assets/cards.json')
    .then(r => r.json())
    .then(data => renderCards(data));

  function renderCards(cards){
    const container = document.getElementById('cards');
    if(!container) return;
    container.innerHTML = '';
    cards.forEach(card => {
      const div = document.createElement('div');
      div.className = 'card';
      div.innerHTML = `
        <h3><a href='/${card.path}'>${card.title}</a></h3>
        <div class="meta">
          ${card.difficulty ? `<span class='badge difficulty'>${card.difficulty}</span>` : ''}
          ${card.os.map(o=>`<span class='badge os'>${o}</span>`).join('')}
          ${card.tags.map(t=>`<span class='badge tag' data-tag='${t}'>${t}</span>`).join('')}
        </div>
        <small>${card.last_updated}</small>
        <div class='actions'>
          <a class='md-button' href='/${card.path}'>Open</a>
          <button class='md-button copy-card' data-path='/${card.path}'>Copy all</button>
        </div>`;
      container.appendChild(div);
    });
    container.querySelectorAll('[data-tag]').forEach(el=>{
      el.addEventListener('click', ()=>filterTag(el.dataset.tag));
    });
  }

  function filterTag(tag){
    const cards = document.querySelectorAll('#cards .card');
    cards.forEach(c=>{
      c.style.display = c.querySelector(`[data-tag='${tag}']`) ? '' : 'none';
    });
  }
});
