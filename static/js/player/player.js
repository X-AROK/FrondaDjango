let playerData;
let currentPlayer;
let currentSeason;
let currentEp;

$.ajax(ajaxUrl)
	.done(function (data) {
		let result = jQuery.parseJSON(data);
		playerData = result;
		console.log(result);

		for (player in result) {
			let playerName = player.charAt(0).toUpperCase() + player.slice(1);
			$('#input-player').append( $('<option>').val(player).text(playerName) );
		}


		let seasonsCount = Object.keys(result[$('#input-player').val()]).length;
		currentPlayer = $('#input-player').val();

		if (seasonsCount < 2) {
			$('#input-season').css('display', 'none');
		} else {
			$('#input-season').css('display', 'inline-block');
			for (season in result[currentPlayer]) {
				$('#input-season').append( $('<option>').val(season).text('Сезон ' + season).addClass('option-season') );
			}
		}
		currentSeason = $('#input-season').val() ? $('#input-season').val() : '1';

		let episodesCount = Object.keys(result[currentPlayer]['1']).length;
		if ( seasonsCount < 2 && episodesCount < 2 ) {
			$('#input-episode').css('display', 'none');
		} else {
			$('#input-episode').css('display', 'inline-block');
			for (episode in result[currentPlayer][currentSeason]) {
				$('#input-episode').append( $('<option>').val(episode).text('Серия ' + episode).addClass('option-episode') );
			}
		}
		currentEp = $('#input-episode').val() ? $('#input-episode').val() : '1';

		$('#player').attr("src", result[currentPlayer][currentSeason][currentEp]);
		$('.loading').css('display', 'none');
	});

$('#input-player').on('change', function () {
	$('.option-episode').remove();
	$('.option-season').remove();
	currentPlayer = $(this).val();

	let seasonsCount = Object.keys(playerData[currentPlayer]).length;

	if (seasonsCount < 2) {
		$('#input-season').css('display', 'none');
	} else {
		$('#input-season').css('display', 'inline-block');
		for (season in playerData[currentPlayer]) {
			$('#input-season').append( $('<option>').val(season).text('Сезон ' + season).addClass('option-season') );
		}
	}
	currentSeason = $('#input-season').val() ? $('#input-season').val() : '1';

	let episodesCount = Object.keys(playerData[currentPlayer]['1']).length;
	if ( seasonsCount < 2 && episodesCount < 2 ) {
		$('#input-episode').css('display', 'none');
	} else {
		$('#input-episode').css('display', 'inline-block');
		for (episode in playerData[currentPlayer][currentSeason]) {
			$('#input-episode').append( $('<option>').val(episode).text('Серия ' + episode).addClass('option-episode') );
		}
	}
	currentEp = $('#input-episode').val() ? $('#input-episode').val() : '1';

	$('#player').attr("src", playerData[currentPlayer][currentSeason][currentEp]);
});

$('#input-season').on('change', function () {
	$('.option-episode').remove();
	currentSeason = $(this).val();

	$('#input-episode').css('display', 'inline-block');
	for (episode in playerData[currentPlayer][currentSeason]) {
		$('#input-episode').append( $('<option>').val(episode).text('Серия ' + episode).addClass('option-episode') );
	}

	currentEp = $('#input-episode').val() ? $('#input-episode').val() : '1';

	$('#player').attr("src", playerData[currentPlayer][currentSeason][currentEp]);
});

$('#input-episode').on('change', function () {
	currentEp = $(this).val();
	$('#player').attr("src", playerData[currentPlayer][currentSeason][currentEp]);
});