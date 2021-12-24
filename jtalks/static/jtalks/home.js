// code to load courses in home.html
$(document).ready(function () {
  $("#load_more").on("click", function () {
    var _currentCourses = $(".product-box").length;
    var _limit = $(this).attr("data-limit");
    var _total = $(this).attr("data-total");
    // start ajax
    $.ajax({
      url: "/load-more-data/",
      data: {
        limit: _limit,
        offset: _currentCourses,
      },
      dataType: "json",
      beforeSend: function () {
        $("#load_more").attr("disabled", true);
        $(".load-more-icon").addClass("fa-spinner");
      },
      success: function (res) {
        $(".course-cards").append(res.data);
        $("#load_more").attr("disabled", false);
        $(".load-more-icon").removeClass("fa-spinner");

        if (_currentCourses == _total) {
          $("#load_more").remove();
          $(".product_end").show();
        }
      },
    });
    // end ajax
  });

  // load more products

  $("#load_more_products").on("click", function () {
    var _currentProducts = $(".card-box").length;
    var _limit = $(this).attr("data-limit");
    var _total = $(this).attr("data-total");

    // start ajax
    $.ajax({
      url: "/load_more_products/",
      data: {
        limit: _limit,
        offset: _currentProducts,
      },
      dataType: "json",
      beforeSend: function () {
        $("#load_more_products").attr("disabled", true);
        $(".load-more-icon").addClass("fa-spinner");
      },
      success: function (res) {
        $(".products-cards").append(res.data);
        $("#load_more_products").attr("disabled", false);
        $(".load-more-icon").removeClass("fa-spinner");

        if (_currentProducts == _total) {
          $("#load_more_products").remove();
          $(".end-products").show();
        }
      },
    });
    // end ajax
  });

  // add course review
  $("form#addForm").submit(function (e) {
    e.preventDefault();
    var _review = $("#id_review_text").val();
    var _rating = $("#id_review_rating option:selected").text();
    var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
    var course_id = $('input[name="course_id"]').val();

    $.ajax({
      url: "/course/save_review/",
      data: {
        id: course_id,
        review: _review,
        rating: _rating,
        csrfmiddlewaretoken: csrfmiddlewaretoken,
      },
      dataType: "json",
      success: function (data) {
        $(".modal").modal("hide");
        $(".hide_btn").hide();
        history.go(0);
      },
    });
  });

  // code to load reviews in course_detail.html
  $("#load_more_review").on("click", function () {
    var _currentReview = $(".review-box").length;
    var _limit = $(this).attr("data-limit");
    var _total = $(this).attr("data-total");
    var _course_id = $(this).attr("data-course-id");

    // start ajax
    $.ajax({
      url: "/course/load_more_review/",
      data: {
        limit: _limit,
        offset: _currentReview,
        id: _course_id,
      },
      dataType: "json",
      beforeSend: function () {
        $("#load_more_review").attr("disabled", true);
        $(".load-more-icon").addClass("fa-spinner");
      },
      success: function (res) {
        $(".review-list").append(res.data);
        $("#load_more_review").attr("disabled", false);
        $(".load-more-icon").removeClass("fa-spinner");

        if (_currentReview == _total) {
          $("#load_more_review").remove();
          $(".review_end").show();
        }
      },
    });
    // end ajax
  });

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

  // search more products

  $("#search_more_products").on("click", function () {
    var _currentProducts = $(".card-box").length;
    var _limit = $(this).attr("data-limit");
    var _total = $(this).attr("data-total");
    var _search = $(this).attr("data-search");

    // start ajax
    $.ajax({
      url: "/search_more_products/",
      data: {
        limit: _limit,
        offset: _currentProducts,
        search: _search,
      },
      dataType: "json",
      beforeSend: function () {
        $("#search_more_products").attr("disabled", true);
        $(".load-more-icon").addClass("fa-spinner");
      },
      success: function (res) {
        $(".products-cards").append(res.data);
        $("#search_more_products").attr("disabled", false);
        $(".load-more-icon").removeClass("fa-spinner");

        if (_currentProducts == _total) {
          $("#search_more_products").remove();
          $(".end-products").show();
        }
      },
    });
    // end ajax
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
    // end ajax
  });
});
