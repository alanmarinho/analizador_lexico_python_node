document.addEventListener('DOMContentLoaded', function () {
  function solicitarDados(input) {
    return fetch(`/api/analizador?input=${encodeURIComponent(input)}`)
      .then(response => response.json())
      .then(data => {
        return data;
      })
      .catch(error => {
        console.error('Erro ao solicitar dados:', error);
        throw error;
      });
  }

  function criarTabela(tokens) {
    let tabela = document.getElementById('table');
    tabela.innerHTML = '';
  
    let table = document.createElement('table');
    let thead = document.createElement('thead');
    let tbody = document.createElement('tbody');
    table.appendChild(thead);
    table.appendChild(tbody);
    
    

    let headerRow = document.createElement('tr');
    headerRow.innerHTML = '<th>TOKEN</th><th>TIPO</th><th>VALOR</th>';
    thead.appendChild(headerRow);
  
    for (let i = 0; i < tokens.length; i++) {
      let row = document.createElement('tr');
      let cellToken = document.createElement('td');
      let cellTipo = document.createElement('td');
      let cellValor = document.createElement('td');
      cellToken.textContent = tokens[i].token;
      cellTipo.textContent = tokens[i].tipo;
      cellValor.textContent = tokens[i].valor;
      row.appendChild(cellToken);
      row.appendChild(cellTipo);
      row.appendChild(cellValor);
      tbody.appendChild(row);
    }
  
    tabela.appendChild(table);
  }
  
  document.getElementById('submit').addEventListener('click', function (event) {
    event.preventDefault();
    const input = document.getElementById('input');
    const expressao = input.value;
    solicitarDados(expressao).then(criarTabela);
  });

});