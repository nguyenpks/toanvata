/* Chèn vào cuối mọi bài học. Cần <body data-lesson-id="..."> và js/progress.js.
   - Bài học nằm trong iframe: gửi postMessage cho trang cha (cùng origin).
   - Bài học mở riêng, cùng origin: ghi trực tiếp vào LocalStorage. */
(function () {
  'use strict';
  var id = document.body.getAttribute('data-lesson-id');
  if (!id) return;
  var box = document.createElement('div');
  box.className = 'mb-complete';
  var btn = document.createElement('button');
  btn.type = 'button';
  btn.textContent = 'Tôi đã học xong bài này';
  var msg = document.createElement('span');
  msg.setAttribute('aria-live', 'polite');
  box.appendChild(btn); box.appendChild(msg);
  document.body.appendChild(box);
  btn.addEventListener('click', function () {
    if (window.parent !== window) {
      window.parent.postMessage({ type: 'mathbridge:lesson-complete', lessonId: id }, window.location.origin);
      msg.textContent = 'Đã gửi xác nhận hoàn thành.';
    } else if (window.MathBridgeProgress) {
      msg.textContent = window.MathBridgeProgress.markComplete(id)
        ? 'Đã lưu hoàn thành trên trình duyệt này.' : 'Không lưu được. Trình duyệt có thể đang chặn LocalStorage.';
    }
  });
})();
