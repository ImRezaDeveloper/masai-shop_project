const csr = document.querySelector('meta[name="csrf-token"]').content;


document.addEventListener('DOMContentLoaded', () => {
  const csrftoken = document.querySelector('meta[name="csrf-token"]').content;

  document.querySelectorAll('.add-favorites').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      e.preventDefault();

      const url = btn.dataset.url;

      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrftoken,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({}),  // هیچ دیتایی نیاز نیست چون همه چیز توی URL و session هست
      });

      if (response.ok) {
        const data = await response.json();
        const icon = btn.querySelector('i');
        const countSpan = btn.querySelector('.like-count');

        // تغییر آیکون
        if (icon) {
          icon.className = data.liked ? 'fa fa-heart' : 'fa fa-heart-o';
        }

        // به‌روزرسانی شمارنده
        if (countSpan) {
          countSpan.textContent = data.like_count;
        }
      } else {
        console.error("AJAX like request failed");
      }
    })
  })
})