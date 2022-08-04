export function GetStaticFile(file) {
    return `/static${file}`
  }

export function CreateArrayFromInt(count=1, limit=10) {

  const pages_count = limit / count 
  console.log("pages_count", pages_count)

  let pages = [];
  for (let i=1; i <= pages_count; i += 1){
    pages.push(i)
  }
  return pages
}