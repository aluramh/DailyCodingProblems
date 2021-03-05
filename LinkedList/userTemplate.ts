const state: any = {}

// EVERYTHING
const user = {
  stepId: null, // onboarding screen
  uuid: null,
  // step 1
  firstName: '',
  middleName: '',
  lastName: '',

  // step 2
  email: '',
  patientRole: '', // myself or guardian
  diagnosis: '',
  diagnosisYear: '',
  onWaitlist: null,

  metastasis: null,
  sherpa: {
    organizationId: null,
    name: null
  },
  // sensitive records types
  mentalHealth: false,
  hivAids: false,
  sexualHealth: false,
  substanceAbuse: false,
  includeSensitiveRecords: true,

  hieConsent: null,

  // from driver license
  gender: null,
  birthDate: null,

  streetAddress: null,
  city: null,
  state: null,
  zipCode: null,

  textMessageConsent: null,
  consent: null,
  researchConsent: null,
  hasPriorNames: null,
  priorNames: '',
  idURL: null,
  signatureURL: null,
  mobileAlerts: 'declined',

  phone: '',
  hasTreatmentProvider: null,
  diagnosisProvider: null,
  treatmentProvider: null,
  treatmentPhysician: null,
  diagnosisPhysician: null,

  // guardian specific
  relationshipToPatient: null, // UI specific state
  patientFirstName: '',
  patientMiddleName: '',
  patientLastName: '',
  patientBirthdate: '',
  patientIsMinor: null,
  guardianOfAdult: null,
  patientIsDeceased: null,
  birthCertificate: null, // url of birth cert
  legalDocument: null, // url of legal document
  deathCertificate: null, // url of death cert
  specialityProvider: null,
  specialityPhysician: null,
  isNeuro: false,

  // ANCHOR: - Other payload
  givenName: state.patientFirstName,
  familyName: state.patientLastName,
  phoneNumber: state.phone,

  // guardian specific keys below
  guardianProfile: {
    givenName: state.firstName,
    middleName: state.middleName,
    familyName: state.lastName,
    phoneNumber: state.phoneNumber,
    priorNames: ''
  }
}

// Only from updateUserProfile()
const useProfile = {
  // Address
  streetAddress: null,
  city: null,
  state: null,
  zipCode: null,

  givenName: state.patientFirstName,
  middleName: state.patientMiddleName,
  familyName: state.patientLastName,
  idURL: state.idURL,
  signatureURL: state.signatureURL,
  birthDate: formattedBirthDate,
  diagnosis: state.diagnosis,
  metastasis: state.metastasis,
  phoneNumber: state.phone,
  gender: state.gender,
  priorNames: state.priorNames,
  onWaitlist: state.onWaitlist,

  birthCertificate: state.birthCertificate,
  legalDocument: state.legalDocument,
  deathCertificate: state.deathCertificate,
  email: state.email,
  patientIsMinor: false,
  guardianOfAdult: false,
  patientIsDeceased: state.patientIsDeceased,

  // Referral info
  chan_id: '',
  chan_type: '',
  chan_name: '',
  chan_vehicle: '',
  chan_campaign: '',
  chan_content: '',

  // guardian specific keys below
  guardianProfile: {
    givenName: state.firstName,
    middleName: state.middleName,
    familyName: state.lastName,
    phoneNumber: state.phoneNumber,
    priorNames: ''
  }
}
