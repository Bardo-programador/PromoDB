# Etapa 1: build da aplicação
FROM node:20-alpine AS builder

# Diretório de trabalho no container
WORKDIR /app

# Copia arquivos de dependências
COPY package.json package-lock.json ./

# Instala dependências
RUN npm ci

# Copia todo o projeto
COPY . .

# Gera o build do SvelteKit
RUN npm run build

# Etapa 2: imagem final para produção
FROM node:20-alpine as production

WORKDIR /app

# Copia apenas os artefatos necessários do builder
COPY --from=builder /app/build ./build
COPY --from=builder /app/package.json ./
COPY --from=builder /app/package-lock.json ./

# Reinstala somente as dependências de produção
RUN npm ci --omit=dev

# Expõe a porta padrão
EXPOSE 5173

# Comando de inicialização
CMD ["npm", "run", "dev", "--", "--open" ]