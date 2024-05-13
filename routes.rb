#For details on the DSL

Rails.application.routes.draw do
    get "about" , to: "about#index"

    get "sign_up", to: "registration#new"
    post "sign_up", to: "registrations#create"

    get "sign_in", to "session#new"
    post "sign_in", to "session#create"

    delete "logout" to "session#destroy"

    root to : "main#index"
end
