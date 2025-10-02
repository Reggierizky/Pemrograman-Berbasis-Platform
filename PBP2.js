function hitungHargaAkhir(totalBelanja) {
  let diskon = 0;

  if (totalBelanja > 1000000) {
    diskon = 0.15; // 15%
  } else if (totalBelanja > 500000) {
    diskon = 0.10; // 10%
  } else {
    diskon = 0; // Tidak ada diskon
  }

  let hargaAkhir = totalBelanja - (totalBelanja * diskon);
  return hargaAkhir;
}

// Contoh penggunaan
console.log(hitungHargaAkhir(499000));  // 400000 (tanpa diskon)
console.log(hitungHargaAkhir(836000));  // 675000 (diskon 10%)
console.log(hitungHargaAkhir(1100000)); // 1275000 (diskon 15%)