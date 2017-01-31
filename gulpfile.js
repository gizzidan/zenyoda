var gulp = require('gulp');
var cleanCSS = require('gulp-clean-css');
var uglify = require('gulp-uglify');

gulp.task('minify-css', function() {
  return gulp.src([
    '/Users/gizzidan/virtualenvs/zenyoda/static/*.css'
  ])
    .pipe(cleanCSS())
    .pipe(gulp.dest('/Users/gizzidan/virtualenvs/zenyoda/static'));
});

gulp.task('uglify', function() {
  return gulp.src([
    '/Users/gizzidan/virtualenvs/zenyoda/static/js/*.js'
  ])
    .pipe(uglify())
    .pipe(gulp.dest('/Users/gizzidan/virtualenvs/zenyoda/static/js'));
});

gulp.task('minify', ['minify-css', 'uglify']);
