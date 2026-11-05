/* Cấu hình MathJax dùng chung cho website và mọi bài học.
   Trong dòng: \( ... \)   Riêng dòng: \[ ... \]
   Gói ams: aligned, cases, matrix, \text, \tag... (có sẵn trong tex-chtml.js, khai báo rõ để không phụ thuộc bản dựng). */
window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]']],
    packages: { '[+]': ['ams', 'noundefined'] },   // noundefined: lệnh sai hiện đỏ tên lệnh thay vì làm hỏng cả công thức
    processEscapes: true,
    tags: 'none'
  },
  chtml: {
    displayOverflow: 'scroll',       // công thức riêng dòng quá rộng: cuộn ngang, không tràn khỏi khung
    mtextInheritFont: true,          // chữ trong \text{...} dùng cùng phông với bài học
    matchFontHeight: true
  },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    renderActions: {
      addMenu: [0, '', '']           // bỏ menu chuột phải: tránh chiếm thao tác chạm trên máy tính bảng
    }
  }
};
