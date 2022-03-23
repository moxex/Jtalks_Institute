
document.addEventListener("DOMContentLoaded", function () {
  const nav = document.querySelector(".navbar");
  const allNavItems = document.querySelectorAll(".nav-link");
  const navList = document.querySelector(".navbar-collapse");
  const btn = document.querySelector(".navbar-toggler");

  function addShadow() {
    if (window.scrollY >= 100) {
      nav.classList.add("nav-bg");
    } else if (window.scrollY == 0) {
      nav.classList.remove("nav-bg");
    }
  }
  function addShadowClick() {
    nav.classList.add("nav-bg");
  }
  allNavItems.forEach((item) =>
    item.addEventListener("click", () => navList.classList.remove("show"))
  );

  btn.addEventListener("click", addShadowClick);
  window.addEventListener("scroll", addShadow);

  // add to user library
  // this should be for payment first, not library
  $("#enroll_btn").on("click", function (e) {
    e.preventDefault();
    let _user_id = $(this).attr("data-user-id");
    let _user = $(this).attr("data-user");
    let _id = $(this).attr("data-course-id");
    let _price = $(this).attr("data-price");

    $.ajax({
      url: "/course/create_user_library/",
      data: {
        user_id: _user_id,
        id: _id,
        price: _price,
      },
      dataType: "json",
      beforeSend: function () {
        $("#enroll_btn").attr("disabled", true);
        $(".load-more-icon").addClass("fa-spinner");
      },
      success: function (data) {
        console.log(data);
        $("#enroll_btn").text("Redirecting... Please Wait");
        window.location.replace("/course/" + _user + "/user_library/");
      },
    });
  });

  // search more courses

  $("#search_more_courses").on("click", function () {
    let _currentCourses = $(".product-box").length;
    var _limit = $(this).attr("data-limit");
    var _total = $(this).attr("data-total");
    var _search = $(this).attr("data-search");

    // start ajax
    $.ajax({
      url: "/course/search_more_courses/",
      data: {
        limit: _limit,
        offset: _currentCourses,
        search: _search,
      },
      dataType: "json",
      beforeSend: function () {
        $("#search_more_courses").attr("disabled", true);
        $(".load-more-icon").addClass("fa-spinner");
      },
      success: function (res) {
        $(".course-cards").append(res.data);
        $("#search_more_courses").attr("disabled", false);
        $(".load-more-icon").removeClass("fa-spinner");

        if (_currentCourses == _total) {
          $("#search_more_courses").remove();
          $(".product_end").show();
        }
      },
    });
  });
});

