document.addEventListener("DOMContentLoaded", function () {
  // Testimonial carousel
  const testimonials = document.querySelectorAll(".testimonial");
  let currentTestimonial = 0;

  function showTestimonial(index) {
    testimonials.forEach((t) => (t.style.display = "none"));
    testimonials[index].style.display = "block";
  }

  function nextTestimonial() {
    currentTestimonial = (currentTestimonial + 1) % testimonials.length;
    showTestimonial(currentTestimonial);
  }

  if (testimonials.length > 0) {
    showTestimonial(currentTestimonial);
    setInterval(nextTestimonial, 5000); 
  }

  // Build page functionality
  const buildForm = document.querySelector(".build-configurator form");
  const componentSelects = document.querySelectorAll(".component-group select");
  const selectedComponentsDiv = document.getElementById("selected-components");
  const totalPriceDiv = document.getElementById("total-price");

  function updateBuildSummary() {
    let totalPrice = 0;
    selectedComponentsDiv.innerHTML = "";

    componentSelects.forEach((select) => {
      const selectedOption = select.options[select.selectedIndex];
      if (selectedOption.value) {
        const name = selectedOption.textContent;
        const price = parseFloat(selectedOption.value);
        totalPrice += price;

        const componentDiv = document.createElement("div");
        componentDiv.textContent = name;
        selectedComponentsDiv.appendChild(componentDiv);
      }
    });

    totalPriceDiv.textContent = `Total: €${totalPrice.toFixed(2)}`;
  }

  componentSelects.forEach((select) => {
    select.addEventListener("change", updateBuildSummary);
  });

  // Initialize build summary
  updateBuildSummary();

  if (buildForm) {
    buildForm.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("Build saved!");
    });
  }

  // Contact form functionality
  const contactForm = document.querySelector(".contact-form-container form");

  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("Thank you for your message. We will get back to you soon!");
      contactForm.reset();
    });
  }

  // Mobile menu toggle
  const navbarToggler = document.querySelector(".navbar-toggler");
  const navbarMenu = document.querySelector(".navbar-menu");

  if (navbarToggler && navbarMenu) {
    navbarToggler.addEventListener("click", function () {
      navbarMenu.classList.toggle("active");
    });
  }
});
