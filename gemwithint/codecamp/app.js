const { GoogleGenerativeAI } = require("@google/generative-ai");

const genAI = new GoogleGenerativeAI("AIzaSyCRUpuFm2Nc17FbHNL-Fv-zNeogCDlqKBg");

async function run() {
  
  const model = genAI.getGenerativeModel({ model: "embedding-001"});
  const text =  "Brown fox jumps over the lazy fox"
  const result = await model.embedContent(text)
  const embedding =  result.embedding
  console.log(embedding)
}

run();