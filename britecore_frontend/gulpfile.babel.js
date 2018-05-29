import gulp from 'gulp';
import jshint from 'gulp-jshint';
import uglify from 'gulp-uglify';
import concat from 'gulp-concat';
import rename from 'gulp-rename';
import browserSync from 'browser-sync';
import useref from 'gulp-useref';

const files = "./src/*.js";

// Task to run jshint of quality verifier
gulp.task('lint', () => {
    return gulp.src(files)
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

// Task to minify, uglify and move the result to ./dist
gulp.task('dist', () => {
    return gulp.src(files)
        .pipe(concat('./dist'))
        .pipe(rename('dist.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('./dist'));
});

gulp.task('useref', function(){
    return gulp.src('app/*.html')
        .pipe(useref())
        .pipe(gulp.dest('dist'))
});

// BrowserSync Init
gulp.task('browserSync', () => {
    browserSync.init({
        server: {
            baseDir: 'app'
        }
    });
});