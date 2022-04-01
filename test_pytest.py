#importação da função testa_numero que está na pasta codigo
from codigo.funcao import testa_numero

#função que fará o teste na função testa_numero
def test_testa_numero():
  entrada = 3
  esperado = 3
  resultado = testa_numero()
  assert resultado == esperado