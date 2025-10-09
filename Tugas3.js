const nama = ["Asep", "Iwan", "Cepi", "Agus", "Dadang"];
const tugas = [80, 75, 70, 65, 60];
const uts = [95, 75, 80, 40, 70];
const uas = [85, 90, 90, 55, 60];

function hitungNA(tugas, uts, uas) {
  return (0.4 * tugas) + (0.3 * uts) + (0.3 * uas);
}

console.log("NO | NAMA SISWA | TUGAS | UTS | UAS | NA");
console.log("-------------------------------------------");

for (let i = 0; i < nama.length; i++) {
  let na = hitungNA(tugas[i], uts[i], uas[i]);
  console.log(
    `${i + 1}  | ${nama[i].padEnd(10)} | ${tugas[i]}   | ${uts[i]}  | ${uas[i]}  | ${na.toFixed(1)}`
  );
}