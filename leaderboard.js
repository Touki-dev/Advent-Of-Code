import fs from 'fs';

let data = JSON.parse(fs.readFileSync('leaderboard.json', 'utf8'));

let members = Object.entries(data.members);
members = members.sort((a, b) => b[1].local_score - a[1].local_score);

var leaderboard = {}
var pos = 0
for (let member of members) {
    pos++
    member = member[1]
    leaderboard[member.name] = pos
}

console.log(Object.keys(leaderboard).length)