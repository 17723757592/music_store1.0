module.exports = {
  root: true,
  parser: '@babel/eslint-parser',
  parserOptions: {
    parser: 'babel-eslint'
  },
  env: {
    browser: true,
    node: true,
    es6: true
  },
  extends: [
    'standard',
    'plugin:vue/essential'
  ],
  plugins: ['vue'],
  rules: {
    'no-unused-vars': 1,
    'no-undef': 1,
    'no-labels': 'off',
    'camelcase': 'off',
    'quote-props': ['warn', 'consistent']
  },
  
}
