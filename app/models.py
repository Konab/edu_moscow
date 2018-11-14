from app import db
from geoalchemy2.types import Geometry


class Super(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), index=True)
	lastname = db.Column(db.String(120), index=True)
	geom = db.Column(Geometry())

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return 'Name: {}'.format(self.name)


class Schools(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# Короткое имя организации
	shortname = db.Column(db.String(70), index=True)
	# Полное имя орагнизации
	fullname = db.Column(db.String(256), index=True)
	# Имя начальника организации
	chiefname  = db.Column(db.String(128), index=True)
	# Email организации
	email = db.Column(db.String(32), index=True)
	# Телефон организации
	publicphone = db.Column(db.String(16), index=True)
	# Веб-сайт орагнизации
	website = db.Column(db.String(32), index=True)
	# Юридический адрес организации
	legaladdress = db.Column(db.String(128), index=True)
	# Организационно-правовая форма
	legalorganization = db.Column(db.String(16), index=True)
	# INN организации
	inn = db.Column(db.String(16), index=True, unique=True)
	# KPP организации
	kpp = db.Column(db.String(16), index=True)
	# IDEKIS организации
	idekis = db.Column(db.String(16), index=True)
	# 
	number = db.Column(db.Integer, index=True)
	# ОГРН организации
	ogrn = db.Column(db.String(16), index=True)
	# Статус организации
	reorganizationstatus = db.Column(db.String(16), index=True)
	# Подчинение 
	subordination = db.Column(db.String(32), index=True)
	# Global ID организации
	global_id = db.Column(db.String(16), index=True)
	############# --Связи-- #############
	# Образовательные программы организации (связь с EducationPrograms)
	educationprograms = db.relationship('EducationPrograms', backref='school', lazy='dynamic')
	# Образовательные услуги (связь с EducationalServices)
	educationalservices = db.relationship('EducationalServices', backref='school', lazy='dynamic')
	# Внутренние экзамены и униформа (связь с EntranceExaminationsAndUniforms)
	entranceexaminationsanduniforms = db.relationship('EntranceExaminationsAndUniforms', backref='school', lazy='dynamic')
	# Адреса корпусов (связь с InstitutionsAddresses)
	institutionsaddresses = db.relationship('InstitutionsAddresses', backref='school', lazy='dynamic')
	# Лицензирование и аккредитация
	licensingandaccreditation = db.relationship('LicensingAndAccreditation', backref='school', lazy='dynamic')
	# Гео данные школ
	geodata = db.relationship('GeoData', backref='school', lazy='dynamic')

	def __repr__(self):
		return 'ShortName: {}, INN: {}, Address: {}'.format(self.shortname, self.inn, self.legaladdress)


class EducationPrograms(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# Образовательная программа
	program = db.Column(db.String(64), index=True)
	# ID организации (связь с табоицей Schools)
	school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))


class EducationalServices(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# Очная форма обучения
	fulltimeedu = db.Column(db.String(16), index=True)
	# Наличие отделения, реализующего основные программы дошкольного образования
	haspreschooledu = db.Column(db.String(16), index=True)
	# Очно-заочная форма обучения
	fullparttimeedu = db.Column(db.String(16), index=True)
	# Экстернат
	externaledu = db.Column(db.String(16), index=True)
	# Семейное образование
	infamilyedu = db.Column(db.String(16), index=True)
	# Обучение на дому
	homebasededu = db.Column(db.String(16), index=True)
	# Заочная форма обучения
	parttimeedu = db.Column(db.String(16), index=True)
	# ID организации (связь с табоицей Schools)
	school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))


class EntranceExaminationsAndUniforms(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# Униформа
	hasuniform = db.Column(db.String(16), index=True)
	# Внутренние экзамены
	hasentrancetest = db.Column(db.String(16), index=True)
	# ID организации (связь с табоицей Schools)
	school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))


class InstitutionsAddresses(db.Model):
	# Информация о корпусе организации
	id = db.Column(db.Integer, primary_key=True)
	# Полное имя организации
	fullname = db.Column(db.String(256), index=True)
	# Имя начальника
	chiefname = db.Column(db.String(128), index=True)
	# Должность начальника
	chiefposition = db.Column(db.String(64), index=True)
	# Административный округ
	admarea = db.Column(db.String(64), index=True)
	# Район
	district = db.Column(db.String(64), index=True)
	# Адрес
	address = db.Column(db.String(128), index=True)
	# Веб-сайт
	website = db.Column(db.String(32), index=True)
	# Телефон
	publicphone = db.Column(db.String(16), index=True)
	# Доступность (связь с таблицей Availability)
	availability = db.relationship('Availability', backref='institutionsaddresses', lazy='dynamic')
	# ID организации (связь с табоицей Schools)
	school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))


class Availability(db.Model):
	id = db.Column(db.Integer, db.ForeignKey('institutions_addresses.id'), primary_key=True)
	# Доступность объекта (инвалиды-опорники)
	available_o = db.Column(db.String(32), index=True)
	# Доступность объекта (инвалиды по зрению)
	available_z = db.Column(db.String(32), index=True)
	# Доступность объекта (инвалиды по слуху)
	available_s = db.Column(db.String(32), index=True)
	# Доступность объекта (инвалиды-колясочники)
	available_k = db.Column(db.String(32), index=True)
	# Элементы доступности (связь с таблицей Available_element)
	available_element = db.relationship('Available_element', backref='availability', lazy='dynamic')
	# institutionsaddresses_id организации (связь с табоицей InstitutionsAddresses)
	# institutionsaddresses_id = db.Column(db.Integer, db.ForeignKey('institutions_addresses.id'))

class Available_element(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# Группа
	group_mgn = db.Column(db.String(64), index=True)
	# Зона учреждения
	area_mgn = db.Column(db.String(64), index=True)
	# Элемент инфраструктуры
	element_mgn = db.Column(db.String(64), index=True)
	# Степень доступности
	available_degree = db.Column(db.String(64), index=True)
	# Показатель доступности
	available_index = db.Column(db.String(64), index=True)
	# availability_id организации (связь с таблицей availability)
	availability_id = db.Column(db.Integer, db.ForeignKey('availability.id'))


class LicensingAndAccreditation(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# Номер бланка аккредитационного свидетельства
	accreditationnumber = db.Column(db.String(32), index=True)
	# Дата окончания срока действия аккредитационного свидетельства
	accreditationexpires = db.Column(db.String(32), index=True)
	# Серия бланка аккредитационного свидетельства
	accreditationseries = db.Column(db.String(32), index=True)
	# Признак наличия лицензии у ОУ
	licenseavailability = db.Column(db.String(32), index=True)
	# Серия бланка лицензии
	licenseseries = db.Column(db.String(32), index=True)
	# Номер бланка лицензии
	licensenumber = db.Column(db.String(32), index=True)
	# Дата окончания срока действия лицензии
	licenseexpires = db.Column(db.String(32), index=True)
	# Признак наличия аккредитационного свидетельства у ОУ
	accreditationavailability = db.Column(db.String(32), index=True)
	# ID организации (связь с табоицей Schools)
	school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))


class GeoData(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# Гео данные школы
	geom = db.Column(Geometry())
	# Центр гео объекта
	center = db.Column(Geometry())
	# ID организации (связь с табоицей Schools)
	school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))
