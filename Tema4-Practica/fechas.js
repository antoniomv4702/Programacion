function calculateDays() {
    const startDate = new Date(document.getElementById('startDate').value);
    const endDate = new Date(document.getElementById('endDate').value);
    const actDate = new Date();
    document.getElementById('fch_ini').innerText = `Fecha.ini: ${startDate}`;
    document.getElementById('fch_fin').innerText = `Fecha.fin: ${endDate}`;
    document.getElementById('fch_act').innerText = `Fecha.act: ${actDate}`;
    if (startDate && actDate) {
        const timeDifference = endDate - actDate;
        const dayDifference = timeDifference / (1000 * 3600 * 24);
        if (dayDifference >= 365) {
            const year = dayDifference / (365);
            const anos = Math.floor(year);
            const dias = dayDifference - (365 * anos)
            document.getElementById('result').innerText = `Hay ${anos} años y ${dias} dias entre las fechas.`;
        } else {
        document.getElementById('result').innerText = `Días entre las fechas: ${dayDifference}`;
        }
    } else {
        document.getElementById('result').innerText = 'Por favor, selecciona ambas fechas.';
    }
}