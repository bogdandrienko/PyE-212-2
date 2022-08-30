rmdir /Q /S production

rename build production

cd ..\

mkdir react

rmdir /Q /S react\production

move frontend\production react\production
