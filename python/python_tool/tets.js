s = "{%27OP1%27%EF%BC%9A%272017-09-14%27;%27OP2%27%EF%BC%9A%272017-09-16%27;%27OP7%27%EF%BC%9A%2725460023%27}".replace(/;/g,',')
JSON.parse(decodeURIComponent(s))
// console.log(decodeURIComponent(s))