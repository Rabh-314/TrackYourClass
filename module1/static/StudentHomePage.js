document.addEventListener('DOMContentLoaded', function() {
    const calendarContainer = document.querySelector(
        '.calendar');
    const today = new Date();
    const todayDate = today.getDate();
    const lastDay = new Date(today.getFullYear(), today
        .getMonth() + 1, 0).getDate();
    let calendarContent =
        `<div class="calendar-header">${today.toLocaleString('default', { month: 'long' })} ${today.getFullYear()}</div>`;
    for (let day = 1; day <= lastDay; day++) {
        const isToday = day === todayDate ? 'today' : '';
        calendarContent +=
            `<div class="day ${isToday}">${day}</div>`;
    }
    calendarContainer.innerHTML = calendarContent;
});

function showContent(index) {
    document.querySelectorAll('.teacher-list').forEach(content => {
      content.style.display = 'none';
    });

    const contentId = 'content' + index;
    document.getElementById(contentId).style.display = 'block';
  }