# Mini-Projeto TrilhaSonora

> **Entrega: sexta-feira, 07/08/2026.**
> Link do repositório no formulário de entrega da aula 09:
> **<https://www.otrilha.com/aulas/09>**. Só o link, nada de zip, nada de email.

Vocês vão construir um analisador do catálogo da **TrilhaSonora**, uma
plataforma fictícia de streaming musical. O resultado é um produto de verdade:
uma classe que modela o catálogo, um menu interativo no terminal e um modo
batch que responde 10 mil consultas de uma vez.

---




ira linha do `main.py`.

Procurar um id percorrendo a lista de 20 mil conteúdos funciona. Fazer isso
10 mil vezes é outra conversa. Um dicionário `{id: conteudo}` construído
**uma vez** no `__init__` transforma essa busca inteira num acesso direto,
e é por isso que o `__init__` recebe o caminho do JSON: ele carrega e
prepara, os outros métodos só consultam.

Pensem em quais dicionários cada um dos 16 métodos precisaria para responder
sem varrer nada. Alguns pedem mais de um índice. Um deles não dá para
indexar de jeito nenhum: descubram qual, e por quê.

---

## Autoverificação (escrita por vocês)

Vocês não precisam esperar a correção para saber se acertaram. No repositório
vem o `gabarito_publico.json`: as respostas **corretas** das 20 primeiras
consultas do `consultas.json`. O formato é o mesmo do `respostas.json` que
vocês vão gerar, id da consulta como chave:

```json
{
  "1": 9.4,
  "2": ["t000003", "t000041"],
  "3": null
}
```

O que a gente **não** entrega é o programa que compara os dois arquivos.
Esse é de vocês. Escrevam um `conferir.py` que abre o `gabarito_publico.json`
e o `respostas.json` de vocês, compara chave por chave e diz quantas bateram
e quais não bateram.

Não é trabalho perdido nem enfeite: é o jeito de vocês pararem de conferir
resposta no olho. Cada vez que mudarem a `Catalogo`, rodar esse script leva
um segundo e responde se vocês quebraram alguma coisa. Sem ele, cada mudança
vira uma rodada de desconfiança.

Duas armadilhas na comparação, que valem para qualquer conferidor de dados:

- **Float não se compara com `==`.** `0.1 + 0.2` não é `0.3` em Python
  (testem no terminal, é real). Comparem a diferença absoluta contra uma
  tolerância pequena, tipo `abs(a - b) < 1e-6`.
- **Resposta ausente não é resposta errada.** Se um id do gabarito nem
  aparece no `respostas.json` de vocês, isso é um bug diferente de ter
  respondido o valor errado. Vale distinguir os dois na saída.

As 20 consultas públicas cobrem vários tipos e alguns casos de borda. Se as
20 baterem, a confiança é alta. Podem commitar o `conferir.py` no repositório:
ele conta a favor de vocês no critério de qualidade.

---

## Antes de entregar

Façam o caminho inteiro numa **cópia limpa** do repositório: clonem o fork de
vocês numa pasta nova, rodem o `main.py` do zero e passem o conferidor de
vocês no `respostas.json` que sair dali.

É o teste mais barato que existe e pega 90% dos problemas de entrega,
principalmente o clássico "funciona na minha pasta porque tem um arquivo que
eu esqueci de commitar".

---

## Como vamos avaliar

A avaliação tem duas dimensões.

### As respostas (piso obrigatório)

O `respostas.json` de vocês precisa estar certo. Esse é o piso: sem isso, o
projeto não está completo, por mais bonito que esteja o código.

Não tem ambiguidade para negociar aqui, porque as 17 regras canônicas estão
todas escritas acima. Toda decisão de caso de borda já foi tomada e está
documentada: o que fazer com id inexistente, com rating ausente, com data no
formato errado, com fila vazia. Se a resposta de vocês difere, é porque uma
das 17 não foi seguida.

### Qualidade (o que eu vou ler)

Eu (João) leio todo o código de vocês. Não é automático, é leitura humana.
Vou olhar quatro coisas:

**Nomes.** `x`, `lista` e `temp` são nomes ruins. `usuario`,
`total_segundos` e `conteudo_atual` são nomes bons. Um nome bom diz o que a
coisa é sem precisar de um comentário ao lado explicando.

**Funções pequenas.** Uma função de 80 linhas que chama outra de 60
geralmente quer dizer que dá para quebrar em partes menores com propósito
único. Cada função deve fazer uma coisa, e o nome dela deve descrever essa
coisa.

**Modelagem.** Cada classe que vocês criarem precisa fazer algo que um
dicionário não faria. Se a justificativa no README for fraca, a classe não
justifica a existência dela.

**Tratamento defensivo na dose certa.** `.get()` onde faz sentido é bom.
`try/except Exception` envolvendo blocos inteiros para "garantir que
funciona" é sinal de que o código não entende o dado que está tratando.
Tratamento defensivo deve ser cirúrgico, não genérico: vocês sabem
exatamente quais são as 7 sujeiras, então tratem essas 7.

Vocês recebem feedback escrito individual depois da correção.

---

## Como entregar

1. Confiram que a raiz do fork tem `catalogo.py`, `main.py`, `cli.py`,
   `respostas.json` e o `README.md` de vocês.
2. Façam o teste da cópia limpa da seção *Antes de entregar* uma última vez.
3. `git push` para o fork de vocês.
4. Mandem **o link do repositório** no formulário de entrega da aula 09:
   <https://www.otrilha.com/aulas/09>

**Prazo: sexta-feira, 07/08/2026.** Se o repositório de vocês for privado,
não esqueçam de nos dar acesso. 

---

## Fechamento

Vocês têm tudo que precisam para construir isso. Comecem pelo
`catalogo_dev.json`, 60 conteúdos, dá para ler com os olhos. Entendam o
que tem dentro, façam funcionar ali, e só depois liguem no
`catalogo_final.json`. Se em algum momento a coisa parecer pesada demais,
voltem no `__init__`: quase sempre a resposta está lá.

Boa construção. Qualquer dúvida, chama a gente.
