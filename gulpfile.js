
// Include gulp
var gulp = require('gulp');

// Include our plugins
var sourcemaps = require('gulp-sourcemaps');
var sass = require('gulp-sass');
var cleanCSS = require('gulp-clean-css');
var rename = require('gulp-rename');
var postcss = require('gulp-postcss');
var stripCssComments = require('gulp-strip-css-comments');
var autoprefixer = require('autoprefixer');
var clean = require('gulp-clean');

//********* TASKS */

// Compile two sass files versions, clean code and create sourcemaps
gulp.task('sass', function(){
    return gulp.src('sass/styles.scss')
        .pipe(sass({
            outputStyle: 'expanded',
        }))
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(postcss([ autoprefixer() ]))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('./static')) // Storage full code file
        .pipe(stripCssComments({preserve: false}))
        .pipe(cleanCSS({debug: true}, (details) => {
            console.log(`${details.name}: ${details.stats.originalSize}`);
            console.log(`${details.name}: ${details.stats.minifiedSize}`);
        }))
        .pipe(rename({
            suffix: ".min"
        }))
        .pipe(gulp.dest('./static')) // Storage minified file
});

// Watch files for changes
gulp.task('watch', function() {
    gulp.watch('sass/**/*.scss', gulp.parallel('sass'))    
});