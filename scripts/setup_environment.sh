#versão do Python
python_version=$(python3 -V 2>&1 | cut -d' ' -f2)
echo "Python version: $python_version"

#remove ambiente existente se houver
if [ -d "venv" ]; then
    echo "Removendo ambiente virtual existente..."
    rm -rf venv
fi

# criar ambiente virtual
echo "Criando ambiente virtual..."
python3 -m venv venv

#ativar ambiente
echo "Ativando ambiente virtual..."
source venv/bin/activate

#atualiza pip e instalar setuptools primeiro
echo "Instala dependências base..."
pip install --upgrade pip
pip install setuptools wheel

#instalar dependências
echo "Instalando dependências do projeto..."
pip install -r requirements.txt

#verificar instalação
echo "Verificando instalação..."
python -c "
try:
    import fastapi, pandas, numpy, pyvis, networkx
    print('Todas as bibliotecas instaladas com sucesso!')
    print(f'FastAPI: {fastapi._version_}')
    print(f'Pandas: {pandas._version_}') 
    print(f'NumPy: {numpy._version_}')
    print(f'NetworkX: {networkx._version_}')
except ImportError as e:
    print(f'Erro: {e}')
    exit(1)
"

echo "Ambiente configurado! Use: source venv/bin/activate"