const workshops = {
  chair: {
    topic: "Repair · 4 places",
    title: "Fix a wobbly chair",
    host: "With Mina Patel",
    time: "Tuesday 21 July, 18:30–20:00",
    place: "North Hall · Step-free entrance · Free",
    description: "Bring one small wooden chair. Basic hand tools are supplied.",
    available: true,
  },
  dumplings: {
    topic: "Food · Fully booked",
    title: "Weeknight dumplings",
    host: "With Asha Lin",
    time: "Thursday 23 July, 19:00–21:00",
    place: "Kitchen Room · Lift access · £8",
    description: "Make and cook two simple fillings. Ingredients and equipment are supplied.",
    available: false,
  },
  herbs: {
    topic: "Garden · 7 places",
    title: "Balcony herbs from cuttings",
    host: "With Leo Grant",
    time: "Saturday 25 July, 10:30–12:00",
    place: "Courtyard · Outdoor level access · £4",
    description: "Prepare mint, rosemary, and thyme cuttings to take home.",
    available: true,
  },
};

const topicFilter = document.querySelector("#topic-filter");
const availabilityFilter = document.querySelector("#availability-filter");
const workshopCards = [...document.querySelectorAll(".workshop")];
const resultCount = document.querySelector("#result-count");
const emptyMessage = document.querySelector("#empty-message");
const dialog = document.querySelector("#workshop-dialog");
const reserveButton = document.querySelector("#reserve-button");
const reservationStatus = document.querySelector("#reservation-status");
let activeWorkshop = null;
let reservationTimer = null;

function updateFilters() {
  let visibleCount = 0;

  for (const card of workshopCards) {
    const matchesTopic = topicFilter.value === "all" || card.dataset.topic === topicFilter.value;
    const matchesAvailability = !availabilityFilter.checked || card.dataset.available === "true";
    const visible = matchesTopic && matchesAvailability;
    card.hidden = !visible;
    visibleCount += Number(visible);
  }

  resultCount.textContent = `${visibleCount} ${visibleCount === 1 ? "workshop" : "workshops"}`;
  emptyMessage.hidden = visibleCount !== 0;
}

function openWorkshop(key) {
  activeWorkshop = workshops[key];
  document.querySelector("#dialog-topic").textContent = activeWorkshop.topic;
  document.querySelector("#dialog-title").textContent = activeWorkshop.title;
  document.querySelector("#dialog-host").textContent = activeWorkshop.host;
  document.querySelector("#dialog-time").textContent = activeWorkshop.time;
  document.querySelector("#dialog-place").textContent = activeWorkshop.place;
  document.querySelector("#dialog-description").textContent = activeWorkshop.description;
  reserveButton.disabled = !activeWorkshop.available;
  reserveButton.textContent = activeWorkshop.available ? "Reserve one place" : "Fully booked";
  dialog.showModal();
}

topicFilter.addEventListener("change", updateFilters);
availabilityFilter.addEventListener("change", updateFilters);

for (const button of document.querySelectorAll(".details-button")) {
  button.addEventListener("click", () => openWorkshop(button.dataset.workshop));
}

reserveButton.addEventListener("click", () => {
  if (!activeWorkshop?.available) return;
  reservationStatus.textContent = `Place reserved for ${activeWorkshop.title}.`;
  window.clearTimeout(reservationTimer);
  reservationTimer = window.setTimeout(() => {
    reservationStatus.textContent = "";
  }, 4000);
  dialog.close();
});

dialog.addEventListener("click", (event) => {
  if (event.target === dialog) dialog.close("cancel");
});
